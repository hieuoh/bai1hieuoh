class nguoi:
    def __init__(self,birday,name,city) :
        self.birday = birday
        self.name = name
        self.city =city
    
    def tinhtuoi(self):
        tuoi = 2024 - self.birday
        print(f'tuoi cua {self.name} la {tuoi}')

def main():
    inputt = int(input("Nhap vao nam ban sinh : "))
    inputtname =input("Nhap vao ten cua ban: ")
    inputtcity = input("Nhap vao thanh pho ban song: ")
    a=nguoi(inputt,inputtname,inputtcity)
    a.tinhtuoi()
main()
        
    
        