# classlarda meros olish bir klassdan ikkinchi klasga usha class husuyatlarnio o'tqazish 

# misol

class Father:
    def __init__(self,gapirish,ishitish,oziqlashish) -> None:
        self.gaprish = gapirish
        self.ishitish = ishitish
        self.oziqlanish = oziqlashish
        
    def gapirish(self):
        print("men gapira olaman")
        

class Soon(Father):
    def __init__(self, gapirish, ishitish, oziqlashish) -> None:
        super().__init__(gapirish, ishitish, oziqlashish)

a =Soon.gapirish()

# bu yerda kurinib turibtiki Fatherdan olingan gapirish metodi Soon classdaham ishlamoqda :)

