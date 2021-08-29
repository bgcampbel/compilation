from pathlib import Path
import os
#import ffmpeg
         
ffmpegCmd1 = '''ffmpeg -i '''
ffmpegCmd2 = ''' -i '''
ffmpegCmd3 = ''' -filter_complex "[0:v]scale=576:1024:force_original_aspect_ratio=1[v0]; [1:v]scale=576:1024:force_original_aspect_ratio=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" -map [v] -map [a] ''' 


ffsizeCommand1 = '''ffmpeg -i '''
ffsizeCommand2 = ''' -vf "scale=576:1024:force_original_aspect_ratio=decrease,pad=576:1024:-1:-1:color=black" '''

ff_fps = ''' -filter:v fps=30 '''

ffprobeCommand = '''ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 '''

output = "/home/beth/Downloads/tikterks/output/"

cmd2 = ''' -vf scale=576:1024,setsar=1:1 '''


pathlist = Path('.').glob('*.mp4')

i = 1

for path in pathlist:
     path_in_str = str(path)
     fullCmd = ffmpegCmd1 + output + str(i-1) + '.mp4' + ffmpegCmd2 + path_in_str + ffmpegCmd3 + output + str(i) + '.mp4'
     print(fullCmd)
     os.system(fullCmd)
     i += 1
     
#for path in pathlist:
    # path_in_str = str(path)
    # fullCmd = ffsizeCommand1 + path_in_str + ff_fps + output + str(i) + '-fps.mp4'
    # os.system(fullCmd)
    # print(fullCmd)
    # i += 1
     
     
     
     
     #delete = 'rm ' + str(i-1) + '.mp4'
     #os.system(delete)
     #print(fullCmd)
     #print(delete)
     #i += 1

#os.system(ffsizeCommand1 + path_in_str + ffsizeCommand2 + i_in_str + '.mp4')

#ffmpeg -i video1.mp4 -i video2.flv -filter_complex "[0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [outv] [outa]" -map "[outv]" -map "[outa]" out.mp4
#ffmpeg -i video1.mp4 -i video2.flv -filter_complex \"[0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [outv] [outa]" \-map "[outv]" -map "[outa]" out.mp4

#ffmpeg -i input.mov -vf scale=576x1026,setdar=1:1 output.mp4

#ffmpeg -i input -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black" output

#ffmpeg -i d:\1.mp4 -i d:\2.mp4 -filter_complex "concat=n=2:v=1:a=1 [v] [a]; [v]scale=320:200[v2]" -map "[v2]" -map "[a]" d:\3.mp4

#ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "[0:v]scale=1024:576:force_original_aspect_ratio=1[v0]; [1:v]scale=1024:576:force_original_aspect_ratio=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" -map [v] -map [a] output.mp4

#ffmpeg -i 0new.mp4 -filter:v fps=30 0fps.mp4

#ffmpeg -i 4-fps.mp4 -vf scale=576:1024,setsar=1:1 4.mp4
 
