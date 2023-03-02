############################################################################################################
# GUI Author: "Marius Selegean"                                                                            #
# Email: "marius.selegean@8x8.com"                                                                         #
# Description: "Add licenses based on licenseId. It copies the values needed and adds them to the SMP."    #
############################################################################################################

####################
# importing packages
####################
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
import sys
import datetime
from functools import partial

###################################
# Root of application and it's name
###################################
root = tk.Tk()
root.title("Add or Remove Licenses")

######################################
#Global Variables used in this program
######################################
credentials = "ODY1ODE5NjE0OTcyOTYzNTpjNGZlMzMzOThlNzc"
customer_id = tk.StringVar
license_id = tk.StringVar
to_add = int

##########
#Functions
##########
# Set the global variables
def set_variables():
    global credentials
#    w1.configure(text = text_entry1.get())
#    credentials = text_entry1.get()
#    print(text_entry1.get())
    global customer_id
 #   w2.configure(text = text_entry2.get())
    customer_id = text_entry2.get()
    print(text_entry2.get())
    global license_id
  #  w3.configure(text= text_entry3.get())
    license_id = text_entry3.get()
    print(text_entry3.get())
    global to_add
   # w4.configure(text = text_entry4.get)
    to_add = text_entry4.get()
    print(text_entry4.get())
    messagebox.showinfo(title="Set Variable", message="Variables successfully set "
                                                      "\n Choose an option Add or Remove Licenses")

# Add Licenses
def add_licenses():
    try:
        global credentials
        global customer_id
        global license_id
        global to_add

        def authentication():  # Getting the token.
            headers = {'Authorization': f'Basic {credentials}', 'Content-Type': 'application/x-www-form-urlencoded'}
            payload = {'grant_type': 'client_credentials', 'scope': 'vo'}
            sso = requests.post(f"https://sso.8x8.com/oauth2/v1/token", headers=headers, data=payload)
            return sso.json()["access_token"]

        bearer = {'Authorization': 'Bearer ' + authentication()}  # Bearer token for the API requests.

        log = open("logs.txt", "a")  # Logging all API requests.

        if not log.writable():  # Checking if we can write the log file.
            messagebox.ERROR("Cannot write to the log file. Exiting the script.")

        start_time = datetime.datetime.now()  # Time it started to add licenses.

        get_license_details = requests.get(f"https://platform.8x8.com/license/v1/customers/{customer_id}/licenses/"
                                           f"{license_id}?scope=expand", headers=bearer)
        if get_license_details.ok:
            if get_license_details.json()['pageResultSize'] == 0:
                log.write(
                    f"[{datetime.datetime.now()}]\tNo results returned for the licenseId provided. Is it correct or "
                    f"does it exist?\n")
                messagebox.ERROR("No results returned for the licenseId provided. Is it correct or does it exist?")
            if 'licensePool' not in get_license_details.json()['content'][0]:
                log.write(f"[{datetime.datetime.now()}]\tThe license does not have any licensePool data in the JSON"
                          f" returned. Exiting the script.\n")
                messagebox.ERROR("The license does not have any licensePool data in the JSON returned. Exiting the script.")
            else:
                license_headers = {
                    'Authorization': 'Bearer ' + authentication(),
                    'Content-Type': 'application/json',
                }
                license_payload = {
                    "packageId": f"{get_license_details.json()['content'][0]['licensePool']['packageId']}",
                    "skuDesc": f"{get_license_details.json()['content'][0]['licensePool']['skuDesc']}",
                    "skuId": f"{get_license_details.json()['content'][0]['licensePool']['skuId']}",
                    "quantity": f"{to_add}",
                    "serviceCountry": f"{get_license_details.json()['content'][0]['licensePool']['serviceCountry']}",
                    "status": "ACTIVE"
                }
                add_licenses = requests.post(f"https://platform.8x8.com/license/v1/customers/{customer_id}/licenses"
                                             f"/_createblock", headers=license_headers, json=license_payload)
                if add_licenses.ok:
                    messagebox.showinfo(title="Adding Licenses", message=(f"Added {to_add} '{get_license_details.json()['content'][0]['licensePool']['name']}' "
                          f"licenses to {customer_id}."))
                    log.write(f"[{datetime.datetime.now()}]\tAdded {to_add} "
                              f"'{get_license_details.json()['content'][0]['licensePool']['name']}' licenses to"
                              f" {customer_id}.\n")
                else:
                    log.write(f"[{datetime.datetime.now()}]\tFailed to add {to_add} "
                              f"'{get_license_details.json()['content'][0]['licensePool']['name']}' licenses "
                              f"to {customer_id}.\t{add_licenses.request.url}\t{add_licenses.request.body}\t"
                              f"{add_licenses.request.headers}\t{add_licenses.status_code}\n")
                    messagebox.ERROR(f"Failed to add the licenses to the customer. Status code: {add_licenses.status_code}.")
        else:
            log.write(f"[{datetime.datetime.now()}]\tFailed to get the license details.\t"
                      f"{get_license_details.request.url}\t{get_license_details.status_code}\n")
            messagebox.ERROR(f"Failed to get the license details. Status code: {get_license_details.status_code}.")

        end_time = datetime.datetime.now()  # Time it ended.
        time_elapsed = end_time - start_time  # Time it took to run the script successfully for all licenses.

        messagebox.showinfo(title="licenses successfully added", message=(f"{to_add} total licenses added in {time_elapsed}."))
        log.write(f"[{datetime.datetime.now()}]\t{to_add} total licenses added in {time_elapsed}.\n")

        log.close()  # Closing the log file.

    except KeyboardInterrupt:
        print("\nThe script has been terminated by the user.")
    except KeyError:
        print("\nOne of the variables is incorrect. Please check and try again.")
    except FileNotFoundError:
        print("\nText file not found. Please create the respective file and try again.")

# Remove Licenses
def remove_licenses():
    try:
        global credentials
        global customer_id
        global license_id
        global to_add # to remove in this case
        times_to_run = int

        def authentication():  # Getting the token.
            headers = {'Authorization': f'Basic {credentials}', 'Content-Type': 'application/x-www-form-urlencoded'}
            payload = {'grant_type': 'client_credentials', 'scope': 'vo'}
            sso = requests.post(f"https://sso.8x8.com/oauth2/v1/token", headers=headers, data=payload)
            return sso.json()["access_token"]

        bearer = {'Authorization': 'Bearer ' + authentication()}  # Bearer token for the API requests.

        log = open("logs.txt", "a")  # Logging all API requests.

        if not log.writable():  # Checking if we can write the log file.
            messagebox.ERROR("Cannot write to the log file. Exiting the script.")

        count = 0  # Counter for all licenses deleted.

        start_time = datetime.datetime.now()  # Time it started to delete licenses.

        # Getting the licensePoolId to delete the licenses from. Step 1.
        get_licensePoolId = requests.get(f"https://platform.8x8.com/license/v1/customers/{customer_id}/licenses/"
                                         f"{license_id}?scope=expand", headers=bearer)
        if get_licensePoolId.ok:
            if get_licensePoolId.json()['pageResultSize'] == 0:
                log.write(
                    f"[{datetime.datetime.now()}]\tNo results returned for the licenseId provided. Is it correct or "
                    f"does it exist?\n")
                messagebox.ERROR("No results returned for the licenseId provided. Is it correct or does it exist?")
            messagebox.showinfo(title="Deleting Licenses", message=(f"Deleting licenses for '{get_licensePoolId.json()['content'][0]['licensePool']['name']}'."))
            licensePoolId = get_licensePoolId.json()["content"][0]["licensePool"]["licensePoolId"]
        else:
            log.write(f"[{datetime.datetime.now()}]\tUnable to run the API. Exiting the script. Step 1.\t"
                      f"{get_licensePoolId.request.url}\t{get_licensePoolId.status_code}\n")
            messagebox.ERROR("Unable to run the API. Exiting the script. Step 1.")

        times_to_run = int(to_add) / 20  # Number of times to run the API.

        # Deleting the licenses. Step 2.
        for i in range(int(times_to_run)):
            delete_licenses = requests.delete(f"https://platform.8x8.com/license/v1/customers/{customer_id}/licenses"
                                              f"?licensePoolId={licensePoolId}&status=PENDING_CONFIGURATION&"
                                              f"count=20", headers=bearer)
            if delete_licenses.ok:
                count += 20
                print(f"{count} '{get_licensePoolId.json()['content'][0]['licensePool']['name']}' licenses deleted.")
                log.write(f"[{datetime.datetime.now()}]\t{count} licenses deleted.\n")
            else:
                log.write(f"[{datetime.datetime.now()}]\tUnable to run the API. Exiting the script.\t"
                          f"{delete_licenses.request.url}\t{delete_licenses.status_code}\n")
                messagebox.ERROR("Unable to run the API. Exiting the script. Step 2.")

        # Deleting the remaining licenses. Step 3.
        if count < int(to_add):
            delete_licenses = requests.delete(f"https://platform.8x8.com/license/v1/customers/{customer_id}/"
                                              f"licenses?licensePoolId={licensePoolId}&status=PENDING_CONFIGURATION&"
                                              f"count={int(to_add) - count}", headers=bearer)
            if delete_licenses.ok:
                count += int(to_add) - count
                print(f"{count} '{get_licensePoolId.json()['content'][0]['licensePool']['name']}' licenses deleted.")
                log.write(f"[{datetime.datetime.now()}]\t{count} licenses deleted.\n")
            else:
                log.write(f"[{datetime.datetime.now()}]\tUnable to run the API. Exiting the script.\t"
                          f"{delete_licenses.request.url}\t{delete_licenses.status_code}\n")
                messagebox.ERROR("Unable to run the API. Exiting the script. Step 3.")

        end_time = datetime.datetime.now()  # Time it ended.
        time_elapsed = end_time - start_time  # Time it took to run the script successfully for all licenses.

        messagebox.showinfo(title="Deleting Licenses", message=(f"{count} total licenses deleted in {time_elapsed}."))
        log.write(f"[{datetime.datetime.now()}]\t{count} total licenses deleted in {time_elapsed}.\n")

        log.close()  # Closing the log file.
    except KeyboardInterrupt:
        print("\nThe script has been terminated by the user.")
    except KeyError:
        print("\nOne of the variables is incorrect. Please check and try again.")
    except FileNotFoundError:
        print("\nText file not found. Please create the respective file and try again.")

# Clear form option
def reset(): # clear form
    for clear in root.winfo_children():
        if isinstance(clear, tk.Entry):
            clear.delete(0, "end")

# Check log option
def open_logfile(): # Open the log file
        with open("logs.txt") as f:
            data = f.readlines()
            tail = data[-10:]
            print(''.join(tail))
        w6=tk.Label(root, text=str(''.join(tail)), height=15, width=75, justify="left")
        w6.grid(row=12, column=0)


###################
# Text Boxes/Labels
###################
"""w1 = tk.Label(root, text="Enter Credentials")
w1.grid(row=0, column=0)
text_entry1 = tk.Entry(root, width=45, borderwidth=5, textvariable=credentials)
text_entry1.grid(row=1, column=0)"""

w2 = tk.Label(root, text="Enter Customer ID")
w2.grid(row=2, column=0)
text_entry2 = tk.Entry(root, width=35, borderwidth=5, textvariable=customer_id)
text_entry2.grid(row=3, column=0)

w3 = tk.Label(root, text="Enter License ID")
w3.grid(row=4, column=0)
text_entry3 = tk.Entry(root, width=35, borderwidth=5, textvariable=license_id)
text_entry3.grid(row=5, column=0)

w4 = tk.Label(root, text="Enter Quantity")
w4.grid(row=6, column=0)
text_entry4 = tk.Entry(root, width=15, borderwidth=5, textvariable=to_add)
text_entry4.grid(row=7, column=0)

w5 = tk.Label(root, text="Instructions: "
                         "\n````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"
                         "\n 1. Enter: Customer ID, License ID and the number\n   "
                         "  of licenses you want to add or remove."
                         "\n 2. Set Variable by pressing the dedicated option"
                         "\n 2. Run needed option Add or Remove Licenses"
                         "\n````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"
                         "\n Note: Credential is the Protected tag token"
                         "\n            License ID is an example of license you want to add or remove"
                         "\n            Check Log option will show you only the last 10 rows from the log file."
                         "\n````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"
                         "\n", justify="left")
w5.grid(row=11, column=0)


#########
# Buttons
#########
b1 = tk.Button(root, text="Set variable", command=set_variables)
b1.grid(row=8, column=0)

b2 = tk.Button(root, text="Add Licenses", command=add_licenses)
b2.grid(row=1, column=1)

b3 = tk.Button(root, text="Remove Licenses", command=remove_licenses)
b3.grid(row=3, column=1)

b4 = tk.Button(root, text="Clear form", command=lambda:reset())
b4.grid(row=9, column=0)

b5 = tk.Button(root, text="Quit", command=root.destroy)
b5.grid(row=9, column=1)

b6 = tk.Button(root, text="Check Log", command=open_logfile)
b6.grid(row=5, column=1)


# End of program
root.mainloop()