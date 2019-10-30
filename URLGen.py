class Generator:

    def AdidasURL(self, model, size):
        BaseSize = 580
        ShoeSize = size - 6.5
        ShoeSize = ShoeSize * 20
        RawSize = ShoeSize + BaseSize
        ShoeSizeCode = int(RawSize)
        URLCreate = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(
            ShoeSizeCode)
        return URLCreate

    def NikeURL(self, model, size):
        # name = str(name).lower()
        # tName = ""
        # flag = 0
        # for i in range(len(name)):
        #     if ord(name[0]) == 32 and flag == 0:
        #         print("Space in the front of the name has been automatically eliminated!!")
        #         flag = 1
        #     elif ord(name[i]) == 32:
        #         tName = tName+"-"
        #     else:
        #         tName = tName + str(name[i])
        print(model + size)