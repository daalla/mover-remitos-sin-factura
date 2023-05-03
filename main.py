"""
1) Elegir carpeta origen
2) Elegir carpeta destino
3) confirmacion: "se copiaran x servicios sin factura de la carpeta <origen> a la carpeta <destino>. desea continuar?"
4) "se copiaran x csrpetas de servicios a carpeta destino"
"""

from pathlib import Path


def choose_source_folder():
    source_path = input("Ingrese la ubicación de la carpeta origen: ")
    return source_path


def choose_destination_folder():
    destination_path = input("Ingrese la ubicación de la carpeta destino: ")
    return destination_path


def get_folders_without_invoice(source_folder):
    print("Analizando la carpeta destino...")

    INVOICE_PATTERN = "factura*"

    services_without_invoice = []

    cursor = Path(source_folder)
    
    # TODO: Agregar exception handling cuando interactuo con sistemas externos
    # (ej, cuando hago llamadas al SO).
    for administration_folder in cursor.iterdir():
        for building_folder in administration_folder.iterdir():
            for service_folder in building_folder:
                invoices = service_folder.glob(INVOICE_PATTERN)
                if not invoices:
                    services_without_invoice += service_folder

    return services_without_invoice


def inform_copy_completion():
    input("Presione Enter para finalizar el programa.")


def inform_copy_cancellation():
    print("Se canceló el proceso de copia.")
    input("Presione Enter para finalizar el programa.")


def main():
    source_folder = choose_source_folder()
    destination_folder = choose_destination_folder()

    folders_without_invoice = get_folders_without_invoice()

    confirmed = ask_for_confirmation()

    if confirmed:
        # habria que validar si ya existn los files en dichas folders antes de sobreescribir
        copy_folders_without_invoice()
        inform_copy_completion()
    else:
        inform_copy_cancellation()


if __name__ == "__main__":
    main()  # Ver si agrego sys.exit, codigos de finalización y aplico ppios unix.
