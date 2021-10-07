# Authors
# Laura Valentina García León - Juan David Murillo
import winreg
import codecs


def decode_registry_keys():
    # Start from "HKEY_CURRENT_USER" and keep going deeper until we reach the "Count" property of the desired registry
    software_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "software")
    microsoft_key = winreg.OpenKey(software_key, "Microsoft")
    windows_key = winreg.OpenKey(microsoft_key, "windows")
    current_version_key = winreg.OpenKey(windows_key, "CurrentVersion")
    explorer_key = winreg.OpenKey(current_version_key, "Explorer")
    user_assist_key = winreg.OpenKey(explorer_key, "UserAssist")
    target_key = winreg.OpenKey(user_assist_key, "{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}")
    count_key = winreg.OpenKey(target_key, "Count")


    for regIndex in range(winreg.QueryInfoKey(count_key)[1]):
        print(winreg.EnumValue(count_key, regIndex)[0])
        rot13 = lambda s: codecs.getencoder("rot13")(s)[0]

        print(rot13(winreg.EnumValue(count_key, regIndex)[0]))
        print("   ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decode_registry_keys()

