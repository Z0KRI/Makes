import argparse

class PermissionMaker:
    def set_positional_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('--model', type=str, help='El modelo del cual se quiere obtener')
        parser.add_argument('--array', type=str, help='Lista de modelos separados por comas')
        parser.add_argument('--file', type=str, help='Archivo relacionado')
        parser.add_argument('--next', type=bool, help="Si debe de añadir permiso para siguiente")
        parser.add_argument('--reject', type=bool, help="Si debe de añadir permiso para rechazar")

    def get_crud(self, args):
        if args.array:
            models = args.array.split(',') if args.array else [args.model]
            for model in models:
                print(f"\n{'-' * 10} {model} {'-' * 10}")
                self.print_crud_statements(model)
                self.print_more_statements(args, model)
        else:
            self.print_crud_statements(args.model)
            self.print_more_statements(args)
    
    def print_crud_statements(self, model):
        crud = ['create', 'read', 'update', 'delete', 'list']
        for i in crud: 
            print(self.query.format(model, i))
        
    def print_more_statements(self, args, model):
        if (args.reject):
            print(self.query.format(model, 'reject'))
        if (args.next):
            print(self.query.format(model, 'next_status'))

    def __init__(self):
        self.query = """INSERT INTO "public".permissions ("name", "guard_name", "created_at") VALUES ('{0}.{1}', 'web', NOW());"""
        parser = argparse.ArgumentParser(description='Generar permisos CRUD para uno o varios modelos.')
        self.set_positional_arguments(parser)
        args = parser.parse_args()
        self.get_crud(args)

if __name__ == '__main__':
    PermissionMaker()
