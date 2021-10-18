text = '8=FIX.4.4|9=123|35=D|34=1|52=20211018-00:41:42.955|60=20211018-00:41:42.955|49=SENDER|56=TARGET|112=TEST|11=FXID1|55=AAPL|54=1|38=123|40=2|10=042'


def fix_to_dict(fix)
    splitted_by_del = fix.split('|')
    pairs = list(map(lambda x: x.split('='), splitted_by_del))
    d = {lst[0]: lst[1] for lst in pairs}
    return d

    
