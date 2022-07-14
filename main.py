import os

src = 'source_folder'
tgt = 'target_folder'

# Extensions lists.
xls = ['.xls', '.xlsx', '.csv', '.xlsm']
pdf = ['.pdf']
ppt = ['.ppt', '.pptx', '.potx']
doc = ['.doc', '.docx']
txt = ['.txt']
msg = ['.msg']
jpg = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif', '.tiff', '.eps']
lnk = ['.lnk']
rar = ['.zip', '.rar', '.7z']
exe = ['.exe', '.msi', '.jar']
iso = ['.iso']
dba = ['.mdb', '.accdb', '.bak', '.conn']
sql = ['.sql']
json = ['.json']

extensions = [*xls, *pdf, *ppt, *doc, *txt, *msg, *jpg, *lnk, *rar, *exe, *iso, *dba, *sql, *json]


def move(file):
    global tgt
    for extension in extensions:
        file = str.lower(file)
        if file.endswith(extension):
            if extension in xls: tgt_folder = 'xls_folder\\'
            if extension in ppt: tgt_folder = 'ppt_folder\\'
            if extension in pdf: tgt_folder = 'pdf_folder\\'
            if extension in doc: tgt_folder = 'doc_folder\\'
            if extension in txt: tgt_folder = 'txt_folder\\'
            if extension in jpg: tgt_folder = 'jpg_folder\\'
            if extension in msg: tgt_folder = 'msg_folder\\'
            if extension in lnk: tgt_folder = 'lnk_folder\\'
            if extension in rar: tgt_folder = 'rar_folder\\'
            if extension in exe: tgt_folder = 'exe_folder\\'
            if extension in iso: tgt_folder = 'iso_folder\\'
            if extension in dba: tgt_folder = 'dba_folder\\'
            if extension in sql: tgt_folder = 'sql_folder\\'
            if extension in json: tgt_folder = 'json_folder\\'
            if not os.path.exists(tgt + tgt_folder): os.makedirs(tgt + tgt_folder)
            os.replace(src + file, tgt + tgt_folder + file)


if __name__ == '__main__':
    for filename in os.listdir(src):
        move(filename)
