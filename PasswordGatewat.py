import argparse

# parser = argparse.ArgumentParser(description='El script esta hecho principalmente para automatizar la creación de las credenciales iniciales para el gateway')
# # Agregar argumentos
# parser.add_argument('--curp', type=str, help='El curp de la persona.')
# parser.add_argument('--name', type=int, help='La nombre de la persona.')
# parser.add_argument('--last_name', type=int, help='Los apellidos de la persona.')

# # Parsear los argumentos
# args = parser.parse_args()

# # Usar los argumentos
# print(f"Hola, {args.nombre}!")
# print(f"Tienes {args.edad} años.")
# print(f"Vives en {args.ciudad}.")


class generate_credentials:
    def setPositionalArguments(self, parser: argparse):
        parser.add_argument('curp', type=str, help='El curp de la persona.')
        parser.add_argument('name', type=int, help='La nombre de la persona.')
        parser.add_argument('last_name', type=int, help='Los apellidos de la persona.')
    
    def __init__(self, argparse: argparse):
        parser = argparse.ArgumentParser(description='El script esta hecho principalmente para automatizar la creación de las credenciales iniciales para el gateway')
        self.setPositionalArguments(parser)
        args = parser.parse_args()
generate_credentials(argparse)