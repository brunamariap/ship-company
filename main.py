def hash(number: int, size: int = 50):
    return number % size


class CrewMember:
    def __init__(self, cpf, code, name, age) -> None:
        self.cpf = cpf
        self.code = code
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"CPF: {self.cpf} \nNome: {self.name} \nIdade: {self.age}"


class CruiseShip:
    def __init__(self) -> None:
        self.__crew = {}
        self.total_number_of_crew = 0
        self.max_number_of_crew = 50

    def insert_crew_member(self, cpf: int, code: int, name: str, age: int):
        if self.total_number_of_crew < self.max_number_of_crew:
            num_hash = hash(cpf)
            if num_hash not in self.__crew:
                self.__crew[num_hash] = CrewMember(cpf, code, name, age)
                self.total_number_of_crew += 1
                # print(self.__crew)
                return True
            else:
                subvector = []

                if type(self.__crew[num_hash]) is list:
                    previus_value = self.__crew[num_hash]
                    if cpf in self.__crew[num_hash]:
                        print("CPF já existe")
                        return None
                else:
                    if cpf == self.__crew[num_hash].cpf:
                        print("CPF já existe")
                        return None
                    # Valor antigo é transformado em lista
                    previus_value = [self.__crew[num_hash]]

                subvector.extend(previus_value)
                subvector.append(CrewMember(cpf, code, name, age))
                self.__crew[num_hash] = subvector
                self.total_number_of_crew += 1
                # print(self.__crew)
                return True
        print("Tripulação máxima atingida")
        return False

    def search_crew_member(self, cpf: int):
        num_hash = hash(cpf)
        if num_hash in self.__crew:
            if type(self.__crew[num_hash]) is not list:
                print('recebido',(cpf))
                print('recebido',type(cpf))
                print('guardado',(self.__crew[num_hash].cpf))
                print('guardado',type(self.__crew[num_hash].cpf))
                if self.__crew[num_hash].cpf == cpf:
                    crew_member = self.__crew[num_hash]
                    print("\n----Dados do tripulante----")
                    print(crew_member)
                    print("-----------------------------")
                    return num_hash
            elif type(self.__crew[num_hash]) is list:
                for i in range(len(self.__crew[num_hash])):
                    if self.__crew[num_hash][i].cpf == cpf:
                        crew_member = self.__crew[num_hash][i]
                        print("\n----Dados do tripulante----")
                        print(crew_member)
                        print("-----------------------------")
                        return num_hash, i, cpf
        return None

    def print_cruise_ship_data(self):
        return f"Tripulação atual: {self.total_number_of_crew} \nTripulação máxima: {self.max_number_of_crew}"


def main():
    import time
    import json
    import random
    from faker import Faker

    fake = Faker()

    max_crew_member = 50
    total_crew_member = 250

    total_cuise_ship = total_crew_member//max_crew_member
    instances_cruise_ship = [CruiseShip() for _ in range(total_crew_member)]

    codes = random.sample(range(1, 251), total_crew_member)
    cpfs = random.sample(range(10000000000, 20000000000), total_crew_member)

    crew_members = {}
    # Criar tripulantes e adicionar em arquivo json
    # with open("crew.json", "w", encoding='utf-8') as crew_data:
    #     for cpf, code in zip(cpfs, codes):
    #         crew_members[cpf] = {
    #             "cpf": cpf,
    #             "code": code,
    #             "name": fake.name(),
    #             "age": random.randrange(18, 60)
    #         }
    #     json.dump(crew_members, crew_data)

    with open("crew.json", 'r', encoding='utf-8') as file_data:
        data_dict = json.loads(file_data.read())

    current_cruise_ship = 0
    current_code = 0

    # for key, value in data_dict.items():
    #     if current_cruise_ship < total_cuise_ship:
    #         if instances_cruise_ship[current_cruise_ship].total_number_of_crew == instances_cruise_ship[current_cruise_ship].max_number_of_crew:
    #             # Encheu o navio
    #             current_cruise_ship += 1

    #         instances_cruise_ship[current_cruise_ship].insert_crew_member(int(key), value['code'], value['name'], value['age'])

    while True:
        print("\n\n--------------------------------")
        print("Selecione uma opção")
        print("A - Inserir tripulante em navio")
        print("S - Pesquisar por tripulante em navio")
        print("Q - Sair")
        option = input("").upper()
        print()

        if option == 'A':
            name = input("Informe o nome do tripulante: ")
            age = int(input("Informe a idade do tripulante: "))
            crew_cpf = int(input("Informe o CPF do tripulante: "))

            if len(str(crew_cpf)) != 11:
                print("Número de CPF inválido")
                continue

            if current_cruise_ship < total_cuise_ship:
                if instances_cruise_ship[current_cruise_ship].total_number_of_crew == instances_cruise_ship[current_cruise_ship].max_number_of_crew:
                    # Encheu o navio
                    current_cruise_ship += 1

                if instances_cruise_ship[current_cruise_ship].insert_crew_member(crew_cpf, codes[current_code], name, age):
                    current_code += 1
                else:
                    print("Erro ao tentar adicionar um novo tripulante")
            else:
                print("Todos os navios estão cheios")
                break

        elif option == 'S':
            search_cpf = int(
                input("Digite o cpf da pessoa a ser encontrada: "))
            if len(str(search_cpf)) != 11:
                print("Número de CPF inválido")
                continue
            else:
                cur_cruise_ship = 0

                # Pesquisa pelo cpf em todos os cruzeiros
                while cur_cruise_ship < total_cuise_ship:
                    crew_exists = instances_cruise_ship[cur_cruise_ship].search_crew_member(
                        search_cpf)
                    if crew_exists is not None:
                        print(f"Cruzeiro: {cur_cruise_ship + 1}")
                        cur_cruise_ship += 1
                        break
                    else:
                        cur_cruise_ship += 1
                else:
                    print("Tripulante não encontrado")
        elif option == 'Q':
            break
        else:
            print("Escolha uma opção válida")


if __name__ == "__main__":
    main()
