import pythoncom
import win32com.client as win32

try:
    # THIS LINE IS MANDATORY IF WE CALLING THE SEND MAIL FROM ANY ASYNC FUNCTIONS / FLASK / GUI Apps
    pythoncom.CoInitialize()
    outlook = win32.Dispatch("Outlook.Application")
    msgloc = outlook.CreateItem(0)
    msgloc.To = to
    msgloc.cc = cc
    msgloc.Subject = subject

    msgloc.HtmlBody = body
    msgloc.BodyFormat = 2
except Exception as e:
    logger.error(f"Error While Preparing Outlook: {e}")
else:
    if attacher_flag:
        try:
            msgloc.Attachments.Add(attachment_location)
        except Exception as e:
            print(f'Error While Adding Attachment To Mail: {e}')

try:
    msgloc.Send()
except Exception as e:
    print(f'Failed Sending Email:{e}')
    return "Failure"
else:
    print('\n=> Task Completed. Mail Sent Successfully.')
    return "Success"
finally:
    pythoncom.CoUninitialize()
