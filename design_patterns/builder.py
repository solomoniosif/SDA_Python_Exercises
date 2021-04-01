class Motherboard:
    def __init__(self, model='xyz'):
        self.model = model

    def __str__(self):
        return self.model


class CPU:
    def __init__(self, model='Snapdragon 888', cores=8):
        self.model = model
        self.cores = cores

    def __str__(self):
        return self.model


class Camera:
    def __init__(self, megapixels, model):
        self.megapixels = megapixels
        self.model = model

    def __str__(self):
        return self.model


class Smartphone:
    def __init__(self):
        self.motherboard = None
        self.cpu = None
        self.camera = None

    def add_motherboard(self, motherboard):
        self.motherboard = motherboard

    def add_cpu(self, cpu):
        self.cpu = cpu

    def add_camera(self, camera):
        self.camera = camera

    def __str__(self):
        return f"Smartphone (Motherboard = {self.motherboard}, Cpu = {self.cpu}, " \
               f"Camera = {self.camera})"


def build_smartphone(motherboard, cpu, camera):
    s = Smartphone()
    s.add_motherboard(motherboard)
    s.add_cpu(cpu)
    s.add_camera(camera)
    return s


if __name__ == '__main__':
    sx1 = Motherboard('SX1')
    sd888 = CPU()
    sony586 = Camera(48, 'Sony IMX 586')

    s = build_smartphone(sx1, sd888, sony586)
    print(s)

    print('* ' * 30)
    imx800 = Camera(64, 'Sony IMX 800')
    s2 = build_smartphone(sx1, sd888, imx800)
    print(s2)
