""" Folosind builder pattern, sa se implementeze procesul de construire a unui calculator
din următoarele componente: placa de baza, procesor, placa video, unitate optica,
sursa de tensiune, ventilator si carcasa."""


#####################################################################################
# Implementation 3. Using an abstract class as an interface for any concrete builder
#####################################################################################

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

    def __str__(self):
        repr_ = 'Computer with the following components:\n'
        for component in self.components:
            repr_ += f"  >>  {component}\n"
        return repr_


class PCBuilder:  # Interface
    def __init__(self, pc=None):
        if pc is None:
            self.pc = PC()
        else:
            self.pc = pc

    def add_motherboard(self, motherboard):
        self.pc.motherboard = motherboard
        self.pc.components.append(motherboard)
        return self

    def add_cpu(self, cpu):
        self.pc.cpu = cpu
        self.pc.components.append(cpu)
        return self

    def add_gpu(self, gpu):
        self.pc.gpu = gpu
        self.pc.components.append(gpu)
        return self

    def add_odd(self, odd):
        self.pc.components.append(odd)
        self.pc.odd = odd
        return self

    def add_psu(self, psu):
        self.pc.components.append(psu)
        self.pc.psu = psu
        return self

    def add_cooler(self, cooler):
        self.pc.cpu_cooler = cooler
        self.pc.components.append(cooler)
        return self

    def add_case(self, case):
        self.pc.case = case
        self.pc.components.append(case)
        return self

    def assemble(self):
        return self.pc


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


if __name__ == '__main__':
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

    pc_builder = PCBuilder()
    my_pc = pc_builder.add_motherboard(aorusX570).add_cpu(ryzen5600x).add_gpu(
            radeonRX6700XT).add_odd(bw_16d1ht).add_psu(rm750x).add_cooler(
            cmHyper212be).add_case(s100tg).assemble()
    print(my_pc)
