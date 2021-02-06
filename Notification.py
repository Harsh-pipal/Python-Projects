from plyer import notification    #importing libraries required
import time
if __name__=='__main__':
    while True:
        notification.notify(
            title="Take Rest!",                                                                                                      
            message='Go and have a walk around, your eyes need some rest. Prolonged computer screen gazing may affect your eyes.',
            app_icon="C:\\Users\\pipal\\OneDrive\\Desktop\\Python Projects\\eyee.ico",                                                #choose your .ico file path
            timeout=10
        )
        time.sleep(2*60*60)
    
