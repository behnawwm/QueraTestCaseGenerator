import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))


path = os.getcwd()

print("Enter Folder Name:")
folderName = input()
path += "\\" + folderName;

try:
    os.mkdir(path)
    path1 = path + "\\in"
    path2 = path + "\\out"
    os.mkdir(path1)
    os.mkdir(path2)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

cnt = 1
while True:
    print("input " + str(cnt) + ":")

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    inp = '\n'.join(lines)

    print("output " + str(cnt) + ":")

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    out = '\n'.join(lines)

    f = open(path1 + "\input" + str(cnt) + ".txt", "w")
    f.write(inp)
    f.close()

    f = open(path2 + "\output" + str(cnt) + ".txt", "w")
    f.write(out)
    f.close()

    print("done? type \"Y\" ")
    if input() == "Y":
        if __name__ == '__main__':
            zipf = zipfile.ZipFile(folderName + '.zip', 'w', zipfile.ZIP_DEFLATED)
            zipdir(path, zipf)
            zipf.close()
        break;

    cnt += 1
print("GG!")
