# QAutoRPALIVE
QAutofamily RPA and Livemonitor

RPA:

1. Generate use case at QAutoflow
2. Transform with RPA options
3. Configure robot RPA_settings.json and define business critical steps
4. Run QAutoRPA-generate-robot-job with RPA_settings.json
   - QAutoRPA-watchdog-job-my_robot_name   
    - QAutoRPA-control-job-my_robot_name
      - QAutoRPA-runrobot-job-my_robot_name
   
Livemonitor:

1. Generate use case at QAutoflow with monitor option
2. File polling job is running every minute
3. Copy file settings and enc to c:\livemonitor folder
4. File polling job launches transform job
 - Clean start workspace
 - Save robot project zip file and save artifact
 - Launch generate livemonitor
5. Livemonitor generate job
 - copy c:\livemonitor setting.json file to workspace
 - Generate livemonitor rob
   - Read settings
    - build period replace from template
   -QAutoLivemonitor-robotnimi
6. now livemonitor is on
