class house:
    def init(self, type_, total_area, names_furniture):
        self.type = type_
        self.total_area = total_area
        self.names_furniture = names_furniture
        self.remaining_area = total_area
    def cali(self):
        for furniture in self.names_furniture:
            if furniture == 'Bed':
                self.remaining_area -= 4
            elif furniture == 'Wardrobe':
                self.remaining_area -= 2
            elif furniture == 'Table':
                self.remaining_area -= 1.5
        print(f'household type: {self.type} total area: {self.total_area} \nremaining area: {self.remaining_area} furniture name: {self.names_furniture}')
house_1=house("asd", 123, ['Bed', 'Wardrobe', 'Table'])
house.cali()