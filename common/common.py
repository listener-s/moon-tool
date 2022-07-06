from translate import Translator


class Common:
    @classmethod
    def chinese_translate(cls, string):
        if string:
            string = string.replace("'", ' ') or string.replace('"', ' ')
        translate_or = Translator(to_lang='chinese')
        translation = translate_or.translate(string)
        return translation

    @classmethod
    def msg(cls, code, msg=None, data=None, **kwargs):
        result = dict()
        result['code'] = int(code) if str(code).isdigit() else 50000
        result['mag'] = kwargs.get('remsg', None) or msg
        if data is not None:
            result['data'] = data
        return result
