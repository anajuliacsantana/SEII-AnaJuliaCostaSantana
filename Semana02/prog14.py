import os

os.chdir('/Users/anaju/Documents/Playlist')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title,f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip().zfill(2)
    #Pesquisar o atalho mostrado no vídeo
    #Alt + botaõ esquerdom mouse para selecionar
    #ctrl + shift+ alt +setas
    new_name = '{}-{}{}'.format(f_num,f_title,f_ext)

    os.rename(f, new_name)



