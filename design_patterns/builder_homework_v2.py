from abc import ABC, abstractmethod


""" Folosind builder pattern, sa se implementeze procesul de construire a unui calculator
din următoarele componente: placa de baza, procesor, placa video, unitate optica,
sursa de tensiune, ventilator si carcasa."""

"""    Parts of the Builder Pattern:
1. Product — The Product being built
2. Concrete Builder — Build the concrete product. Implements the IBuilder interface
3. Builder Interface — The Interface which the Concrete builder should implement
4. Director — Has a construct method which when called creates a customised product
"""


#####################################################################################
# Implementation 2. Using an abstract class as an interface for any concrete builder
#####################################################################################


class Motherboard:
    def __init__(self, model_name=None, form_factor='ATX', cpu_socket='AM4',
                 chipset='X570', usb_ports=8):
        self.model_name = model_name
        self.form_factor = form_factor
        self.cpu_socket = cpu_socket
        self.chipset = chipset
        self.usb_ports = usb_ports

    def __str__(self):
        return f"Motherboard {self.model_name}, {self.form_factor}, {self.chipset} " \
               f"chipset with {self.cpu_socket} socket and {self.usb_ports} USB ports."


class CPU:
    def __init__(self, manufacturer=None, model_name=None, frequency=None, cores=6):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.frequency = frequency
        self.cores = cores

    def __str__(self):
        return f"CPU {self.model_name} by {self.manufacturer}, " \
               f"{self.frequency} Mhz, {self.cores} cores."


class GPU:
    def __init__(self, manufacturer=None, model_name=None, memory_type=None,
                 memory_size=None, tdp=None):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.memory_type = memory_type
        self.memory_size = memory_size
        self.tdp = tdp

    def __str__(self):
        return f"GPU {self.model_name} by {self.manufacturer} " \
               f"with {self.memory_size} GB of {self.memory_type} memory."


class ODD:
    def __init__(self, manufacturer=None, type_=None):
        self.manufacturer = manufacturer
        self.type_ = type_

    def __str__(self):
        return f"Optical Disc Drive: {self.type_} manufactured by {self.manufacturer}."


class PSU:
    def __init__(self, manufacturer=None, model_name=None, wattage=None,
                 efficiency_rating=None, modularity=False):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.wattage = wattage
        self.efficiency_rating = efficiency_rating
        self.modularity = modularity

    def __str__(self):
        return f"{self.model_name} Power Supply Unit by {self.manufacturer} with " \
               f"{self.wattage}W power output, {self.efficiency_rating} efficiency rating."


class CPUCooler:
    def __init__(self, manufacturer=None, model_name=None, cooling_type=None,
                 fan_speed=None, fan_noise=None):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.cooling_type = cooling_type
        self.fan_speed = fan_speed
        self.fan_noise = fan_noise

    def __str__(self):
        return f"{self.model_name} CPU Cooler by {self.manufacturer} with " \
               f"{self.cooling_type} cooling, {self.fan_speed} RPM fan speed, " \
               f"and {self.fan_noise} dB fan noise."


class ComputerCase:
    def __init__(self, manufacturer=None, model_name=None, form_factor=None):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.form_factor = form_factor

    def __str__(self):
        return f"{self.model_name} {self.form_factor} " \
               f"computer case from {self.manufacturer}."


class PC:
    def __init__(self):
        self.motherboard = None
        self.cpu = None
        self.gpu = None
        self.odd = None
        self.psu = None
        self.cpu_cooler = None
        self.case = None

    def __str__(self):
        result = 'Computer with the following components:\n'
        result += f"  >>  {self.motherboard}\n"
        result += f"  >>  {self.cpu}\n"
        result += f"  >>  {self.gpu}\n"
        result += f"  >>  {self.odd}\n"
        result += f"  >>  {self.psu}\n"
        result += f"  >>  {self.cpu_cooler}\n"
        result += f"  >>  {self.case}\n"
        return result


class AbstractBuilder(ABC):
    def __init__(self):
        self.pc = PC()

    def create_new_pc(self):
        self.pc = PC()

    @abstractmethod
    def add_motherboard(self):
        pass

    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_gpu(self):
        pass

    @abstractmethod
    def add_odd(self):
        pass

    @abstractmethod
    def add_psu(self):
        pass

    @abstractmethod
    def add_cpu_cooler(self):
        pass

    @abstractmethod
    def add_case(self):
        pass


class MyPCBuilder(AbstractBuilder):

    def add_motherboard(self):
        self.pc.motherboard = Motherboard(model_name='X570 AORUS ELITE',
                                          form_factor='Micro-ATX', cpu_socket='AM4',
                                          chipset='X570', usb_ports=8)

    def add_cpu(self):
        self.pc.cpu = CPU(manufacturer='AMD', model_name='AMD Ryzen™ 5 5600X',
                          frequency=4.6, cores=6)

    def add_gpu(self):
        self.pc.gpu = GPU(manufacturer='AMD', model_name='Radeon RX 6700 XT',
                          memory_type='GDDR6', memory_size=12, tdp=230)

    def add_odd(self):
        self.pc.odd = ODD(manufacturer='Asus', type_='Blu-Ray')

    def add_psu(self):
        self.pc.psu = PSU(manufacturer='Corsair', model_name='RM750x', wattage=750,
                          efficiency_rating='80 Plus Gold', modularity=True)

    def add_cpu_cooler(self):
        self.pc.cpu_cooler = CPUCooler(manufacturer='Cooler Master', cooling_type='air',
                                       model_name='Hyper 212 Black Edition',
                                       fan_speed=2000, fan_noise=26)

    def add_case(self):
        self.pc.case = ComputerCase(manufacturer='Thermaltake', model_name='S100TG',
                                    form_factor='Micro-ATX')


class Director:
    def __init__(self, builder):
        self._builder = builder

    def assemble(self):
        self._builder.add_motherboard()
        self._builder.add_cpu()
        self._builder.add_gpu()
        self._builder.add_odd()
        self._builder.add_psu()
        self._builder.add_cpu_cooler()
        self._builder.add_case()
        return self._builder.pc


if __name__ == "__main__":
    my_pc = MyPCBuilder()
    director = Director(my_pc)

    pc1 = director.assemble()
    print(pc1)
