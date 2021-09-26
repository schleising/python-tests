class AutoDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__ # type: ignore
    __delattr__ = dict.__delitem__ # type: ignore

ad = AutoDict()

ad.test = 'Testing'

print(ad.test) # type: ignore

