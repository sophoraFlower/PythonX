# coding=utf-8
import os


class DosCmd:
    @classmethod
    def excute_cmd_result(self, command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    @classmethod
    def excute_cmd(self, command):
        os.system(command)


if __name__ == '__main__':
    dos = DosCmd()
    print(dos.excute_cmd_result('adb devices'))
