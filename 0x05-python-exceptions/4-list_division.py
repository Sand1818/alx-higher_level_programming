#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nuwe_l = []
    for i in range(list_length):
        try:
            out_p = my_list_1[i] / my_list_2[i]
        except TypeError:
            out_p = 0
            print("wrong type")
        except ZeroDivisionError:
            out_p = 0
            print("division by 0")
        except IndexError:
            out_p = 0
            print("error")
        finally:
            nuwe_l.append(out_p)
    return nuwe_l
