from moviepy.editor import VideoFileClip, concatenate_videoclips


""" make_clip_video(path(원본 비디오 경로), clip_name(clip video name), start_time, end_time) """
def make_clip_video(path, save_path, start_t, end_t):
    clip_video = VideoFileClip(path).subclip(start_t, end_t)
    clip_video.write_videofile(save_path)

path1 = ''
path2 = ''
path3 = ''
path4 = ''


""" 영상 clip """
# 원천 데이터 CCTV 영상은 각도만 다른 동알한 영상이 3~4개씩 있다.
#The original data CCTV image has three to four identical images with different angles.

#1
make_clip_video(path1, 'b_081_pocket_36.mp4', 22, 34)
make_clip_video(path1, 'b_082_pocket_30.mp4', 41, 51)
#
make_clip_video(path1, 'b_081_normal_36.mp4', 4, 16)
make_clip_video(path1, 'b_082_normal_30.mp4', 11, 21)


#2
make_clip_video(path2, 'b_083_pocket_36.mp4', 22, 34)
make_clip_video(path2, 'b_084_pocket_30.mp4', 41, 51)
#
make_clip_video(path2, 'b_083_normal_36.mp4', 4, 16)
make_clip_video(path2, 'b_084_normal_30.mp4', 11, 21)
#

#3
make_clip_video(path3, 'b_085_pocket_36.mp4', 22, 34)
make_clip_video(path3, 'b_086_pocket_30.mp4', 41, 51)
#
make_clip_video(path3, 'b_085_normal_36.mp4', 4, 16)
make_clip_video(path3, 'b_086_normal_30.mp4', 11, 21)
#

#4
make_clip_video(path4, 'b_087_pocket_36.mp4', 22, 34)
make_clip_video(path4, 'b_088_pocket_30.mp4', 41, 51)
#
make_clip_video(path4, 'b_087_normal_36.mp4', 4, 16)
make_clip_video(path4, 'b_088_normal_30.mp4', 11, 21)
#


""" 동일한 영상 내 생성한 clip 붙이기 """
#1
# 이어 붙일 데이터1
abnormal1 = VideoFileClip("b_081_pocket_36.mp4")
abnormal2 = VideoFileClip("b_082_pocket_30.mp4")
# 이어 붙일 데이터2
normal1 = VideoFileClip("b_081_normal_36.mp4")
normal2 = VideoFileClip("b_082_normal_30.mp4")
# 이어 붙일 데이터 합치기
combined_a = concatenate_videoclips([abnormal1, abnormal2])
combined_n = concatenate_videoclips([normal1, normal2])
# 합친 데이터 생성(현재 폴더에 저장)
combined_a.write_videofile("bcom_019_pocket_66.mp4")
combined_n.write_videofile("bcom_019_normal_66.mp4")


#2
abnormal1 = VideoFileClip("b_083_pocket_36.mp4")
abnormal2 = VideoFileClip("b_084_pocket_30.mp4")

normal1 = VideoFileClip("b_083_normal_36.mp4")
normal2 = VideoFileClip("b_084_normal_30.mp4")

combined_a = concatenate_videoclips([abnormal1, abnormal2])
combined_n = concatenate_videoclips([normal1, normal2])

combined_a.write_videofile("bcom_020_pocket_66.mp4")
combined_n.write_videofile("bcom_020_normal_66.mp4")

#3
abnormal1 = VideoFileClip("b_085_pocket_36.mp4")
abnormal2 = VideoFileClip("b_086_pocket_30.mp4")
# 
normal1 = VideoFileClip("b_085_normal_36.mp4")
normal2 = VideoFileClip("b_086_normal_30.mp4")
# 

combined_a = concatenate_videoclips([abnormal1, abnormal2])
combined_n = concatenate_videoclips([normal1, normal2])

combined_a.write_videofile("bcom_021_pocket_66.mp4")
combined_n.write_videofile("bcom_021_normal_66.mp4")

#4
abnormal1 = VideoFileClip("b_087_pocket_36.mp4")
abnormal2 = VideoFileClip("b_088_pocket_30.mp4")
# 
normal1 = VideoFileClip("b_087_normal_36.mp4")
normal2 = VideoFileClip("b_088_normal_30.mp4")
#

combined_a = concatenate_videoclips([abnormal1, abnormal2])
combined_n = concatenate_videoclips([normal1, normal2])

combined_a.write_videofile("bcom_022_pocket_66.mp4")
combined_n.write_videofile("bcom_022_normal_66.mp4")