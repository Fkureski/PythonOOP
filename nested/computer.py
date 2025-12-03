#Creating class main

class Computer:
    def __init__(self, model, gpu_name, gpu_memory, cpu_name, cpu_cores, cpu_clock):
        self.model = model
        self.gpu_name = gpu_name
        self.gpu = self.GPU(gpu_name, gpu_memory)
        self.cpu = self.CPU(cpu_name, cpu_cores, cpu_clock)
    
    def show_configuration(self):
        print(f'Computer: {self.model}')
        self.gpu.show_gpu()
        self.cpu.show_cpu()
        

    class GPU: #Nested class
        def __init__(self, name, memory_gb):
            self.name = name
            self.memory_gb = memory_gb
        def show_gpu(self):
            print(f'GPU: {self.name} Gigabytes: {self.memory_gb}')

    class CPU:
        def __init__(self, name, cores, clock_ghz):
            self.name = name
            self.cores = cores
            self.clock_ghz = clock_ghz
        def show_cpu(self):
            print(f'CPU: {self.name} Cores: {self.cores} Clock: {self.clock_ghz}')

#Utilization

pc1 = Computer('Dell XPS', 'NVIDIA RTX 4090', 24, 'Intel Core i7', 8, 4.6)
pc1.show_configuration()
