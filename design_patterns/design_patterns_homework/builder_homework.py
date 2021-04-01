""" Folosind builder pattern, sa se implementeze procesul de construire a unui calculator
din următoarele componente: placa de baza, procesor, placa video, unitate optica,
sursa de tensiune, ventilator si carcasa."""


#########################################################################
# Implementation 1. Using a class for each component of the final objects
#########################################################################

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
        self.components = []

    def add_motherboard(self, motherboard):
        self.motherboard = motherboard

    def add_cpu(self, cpu):
        self.cpu = cpu

    def add_gpu(self, gpu):
        self.gpu = gpu

    def add_odd(self, odd):
        self.odd = odd

    def add_psu(self, psu):
        self.psu = psu

    def add_cpu_cooler(self, cpu_cooler):
        self.cpu_cooler = cpu_cooler

    def add_case(self, case):
        self.case = case

    def build_pc(self, motherboard=None, cpu=None, gpu=None, odd=None, psu=None,
                 cpu_cooler=None, case=None):
        if motherboard:
            self.add_motherboard(motherboard)
            self.components.append(str(motherboard))
        if cpu:
            self.add_cpu(cpu)
            self.components.append(str(cpu))
        if gpu:
            self.add_gpu(gpu)
            self.components.append(str(gpu))
        if odd:
            self.add_odd(odd)
            self.components.append(str(odd))
        if psu:
            self.add_psu(psu)
            self.components.append(str(psu))
        if cpu_cooler:
            self.add_cpu_cooler(cpu_cooler)
            self.components.append(str(cpu_cooler))
        if case:
            self.add_case(case)
            self.components.append(str(case))

        return self

    def __str__(self):
        repr_ = 'Computer with the following components:\n'
        for component in self.components:
            repr_ += f"  >>  {component}\n"
        return repr_


if __name__ == "__main__":
    aorusX570 = Motherboard(model_name='X570 AORUS ELITE', form_factor='Micro-ATX',
                            cpu_socket='AM4', chipset='X570', usb_ports=8)
    ryzen5600x = CPU(manufacturer='AMD', model_name='AMD Ryzen™ 5 5600X',
                     frequency=4.6, cores=6)
    radeonRX6700XT = GPU(manufacturer='AMD', model_name='Radeon RX 6700 XT',
                         memory_type='GDDR6', memory_size=12, tdp=230)
    bw_16d1ht = ODD(manufacturer='Asus', type_='Blu-Ray')
    rm750x = PSU(manufacturer='Corsair', model_name='RM750x', wattage=750,
                 efficiency_rating='80 Plus Gold', modularity=True)
    cmHyper212be = CPUCooler(manufacturer='Cooler Master', cooling_type='air',
                             model_name='Hyper 212 Black Edition', fan_speed=2000,
                             fan_noise=26)
    s100tg = ComputerCase(manufacturer='Thermaltake', model_name='S100TG',
                          form_factor='Micro-ATX')

    my_pc = PC()
    my_pc = my_pc.build_pc(aorusX570, ryzen5600x, radeonRX6700XT, bw_16d1ht, rm750x,
                           cmHyper212be, s100tg)
    print(my_pc)
