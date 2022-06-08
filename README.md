# Website_Blocker
Python script to block specified websites

Program Architecture

Mac and Linux: /etc/hosts

Windows: C:\Windows\System32\drivers\etc\hosts

How to use Website_Blocker:

  Run cmd as ADMINISTRATOR then 'cd' to the folder with '.py' file and run file with 'python website_blocker.py'
  
  (You can specify parameters of time range and add your websites url's.)
    
    or
  
  Add task in Windows Task Scheduler (Run with highest privileges) --> New Trigger (at startup) --> New Action (start a program) specify filepath for 'website_blocker.pyw'.
  
  (If you want to specify parameters of time range and add your websites url's in this scenario, you have to write them down in file)
