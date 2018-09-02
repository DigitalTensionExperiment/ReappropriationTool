import hcl

class SkeletonComments():



    def __init__(self):
        self.path = '/Users/zwilhelm/Documents/mycode/ReappropriationTool'



    def exraction(self, file):

        file = self.path + file

        with open(file, 'r+') as f:
            print(f) # <_io.TextIOWrapper
                        # name='/Users/zwilhelm/Documents/mycode/ReappropriationTool/template.hcl'
                        # mode='r+'
                        # encoding='UTF-8'>
            d = hcl.load(f)

            print(type(d))
            print(d)

            # for line in f.readlines():
            #
            #     if '#' in line and line.split("#")[0].isspace():
            #
            #         print(line)

                # line.split("#")
                # if "#" in line and line.split("#"):
                #     # print(len(line.split("#")[0]))
                #     print(line.split("#"))

                    #if not line.split("#")[0].isspace():



                    # print(len(line))
                    # print(line)




        # new_version = self.iterate_subvalue(str(current_version))
        # d['version'] = new_version
        # package_config = json.dumps(d, indent=4)

        # with open(self.file_path, 'w') as f:
        #     f.write(package_config)
        # return new_version

        # delete each line that doesn't begin with "#"
