"""
1) Elegir carpeta origen
2) Elegir carpeta destino
3) confirmacion: "se copiaran x servicios sin factura de la carpeta <origen> a la carpeta <destino>. desea continuar?"
4) "se copiaran x csrpetas de servicios a carpeta destino"


Hacer tipo TDD pero "inverso"? Hacer el código, armar los tests y luego 
refactorearlo? Capaz sirve como introducción a TDD
"""

import pathlib


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

    main_folder = pathlib.Path(source_folder)
    
    # TODO: 
    # - Agregar exception handling cuando interactuo con sistemas externos
    # (ej, cuando hago llamadas al SO).
    # - Ver tema del NotADirectoryError cuando toma un elemento que
    # no es un directorio.
    # - Qué pasa cuando un dir está vacío? parece que no se rompe.
    # - Preguntar si hay que mover directorios vacíos tmb (o sea, que no
    # tienen remito). Por el momento, voy a tomar que sí.
    # - Ver si paso todas las constantes a un archivo de config.
    for administration_folder in main_folder.iterdir():
        if administration_folder.is_dir():
            for building_folder in administration_folder.iterdir():
                if building_folder.is_dir():
                    for service_folder in building_folder.iterdir():
                        if service_folder.is_dir():
                            invoices = list(service_folder.glob(INVOICE_PATTERN))
                            if not invoices:
                                services_without_invoice.append(service_folder)

    return services_without_invoice


def inform_copy_completion():
    input("Presione Enter para finalizar el programa.")


def inform_copy_cancellation():
    print("Se canceló el proceso de copia.")
    input("Presione Enter para finalizar el programa.")


def main():
    source_folder = choose_source_folder()
    # TODO: Validar inputs de terceros y usuario?
    destination_folder = choose_destination_folder()

    folders_without_invoice = get_folders_without_invoice(source_folder)

    confirmed = ask_for_confirmation()

    if confirmed:
        # habria que validar si ya existn los files en dichas folders antes de sobreescribir
        copy_folders_without_invoice()
        inform_copy_completion()
    else:
        inform_copy_cancellation()


if __name__ == "__main__":
    main()  # Ver si agrego sys.exit, codigos de finalización y aplico ppios unix.
