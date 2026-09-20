class teacher:
    def readsub(self):#Original Method
        print("Teacher adivses to read 2 hours")
class perfectStudent:
    def readsub(self):#overridder method
        print("Read good")
class lazyStudent:
    def readsub(self):#overridder method
        print("Read not good")
s=teacher()
s.readsub()
s=perfectStudent()
s.readsub()
s=lazyStudent()
s.readsub()