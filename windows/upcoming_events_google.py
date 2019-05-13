import tkinter as tk



def upcoming_events():
    try:
        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
            service = build('calendar', 'v3', http=creds.authorize(Http()))
            now = datetime.datetime.utcnow().isoformat() + 'z' # 'Z' indicates UTC time
            root = tk.Tk()
            root.title("Top 10 Upcoming Events")
            
            events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=10, singleEvents=True,orderBy='startTime').execute()
            events = events_result.get('items', [])
            
            if not events:
                w = tk.Label(root, text="No upcoming events found.")
                w.pack()
		
	    w = tk.Label(root, text="Event Title")	
            w.grid(row=0, column=1)
            w = tk.Label(root, text="Time And Date Of Event")
            w.grid(row=0, column=2)
            
            i=1
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                w = tk.Label(root, text=event['summary'])
                w.grid(row=i, column=1)
                w = tk.Label(root, text=start)
                w.grid(row=i, column=2)
                i=i+1
                
            oot.geometry("400x400")
            root.mainloop()
        except:
            print("Unable to take upcoming events")

	
