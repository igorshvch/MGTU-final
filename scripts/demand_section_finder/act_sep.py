try:
    import cd_processing.textextrconst as tec
except ModuleNotFoundError:
    import textextrconst as tec
import re

pattern_clean = r'-{66}\nКонсультантПлюс.+?-{66}\n'
pattern_sep = r'\n\n\n-{66}\n\n\n'

my_path = r'C:\Python36\1974 Acts.txt'

class ActSep():
    def __init__(self,
                 my_path=my_path,
                 pattern_clean=pattern_clean,
                 pattern_demd_sep = tec.demand_find_pattern,
                 pattern_sep=pattern_sep):
        self.cleaned = ''
        self.demand_store = []
        self.path = my_path
        self.pattern_clean = pattern_clean
        self.patterm_demd_sep = pattern_demd_sep
        self.pattern_sep = pattern_sep
        self.store = []
        self.text_clean()
        self.acts_separation()
        

    def text_clean(self):
        with open(self.path) as file:
            text = file.read()[1:-71]
        self.cleaned = re.subn(self.pattern_clean,
                                repl='',
                                string=text,
                                flags=re.DOTALL)[0]
        print('Text is cleaned. {} file was used.'.format(self.path))

    def acts_separation(self):
        self.store = re.split(self.pattern_sep, string=self.cleaned)
        acts_num = len(self.store)
        self.cleaned = None
        print('Text is separated. '+
              'There are {} acts. '.format(acts_num)+
              'Cleaned text is deleted.')


    def demands_separation(self, border_list):
        re_object = re.compile(self.patterm_demd_sep)
        for i in range(border_list[0], border_list[1], 1):
            match = re_object.search(self.store[i])
            if match:
                self.demand_store.append(match.group(0))
        print('Demands\' search is completed. '+
              '{} demands are found. '.format(len(self.demand_store)))
        return self.demand_store

    def other_parts(self, border_list, par_num):
        holder = []
        for i in self.store[slice(border_list[0],border_list[1])]:
            i = i.split('\n')
            try:
                holder.append(i[par_num])
            except IndexError:
                pass
        print ('{} parts were extracted'.format(len(holder)))
        return holder
            
