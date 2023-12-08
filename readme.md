## Python script for sorting files

This project is a Python script that sorts files into categories based on their extension. It also unpacks archives and removes empty folders.

**Features:**

* Supports multiple categories: images, videos, documents, audio, archives, and other
* Uses transliteration to normalize filenames for non-English characters
* Logs all actions performed by the script
* Uses threads to improve performance

**Technologies Used:**

* Python 3.11
* shutil, pathlib, sys, os, threading, logging

### Threads:

The script uses threads to improve performance. This allows the script to process multiple files simultaneously.

### Output:

The script will create a folder for each category and move files to the appropriate folder. It will also print a summary of the number of files in each category.


### Logging:

The script logs all actions performed at the `INFO` level. You can configure the logging level to `DEBUG` for more detailed information.

### Log Examples

<details>
<summary>INFO level</summary>

 
```commandline
[2023-12-08 15:07:19,148] INFO MainThread Started sorting folder C:\Work\test_for_sort
[2023-12-08 15:07:19,789] INFO MainThread Starting unpacking archives
[2023-12-08 15:07:19,826] INFO MainThread Deleting empty folders
[2023-12-08 15:07:19,827] INFO MainThread Counting files in folders C:\Work\test_for_sort
[2023-12-08 15:07:19,827] INFO MainThread ------------------------- Sorting results -------------------------
[2023-12-08 15:07:19,827] INFO MainThread Known extensions: .mp3, .xlsx, .txt, .jpg, .docx, .mp4, .zip, .odt, .ogg, .wmv, .ppt, .pdf, .doc, .gif, .mov, .png, .ods, .avi, .csv, .wav, .xls
[2023-12-08 15:07:19,827] INFO MainThread Unknown extensions: .odp, .rar, .tiff
[2023-12-08 15:07:19,827] INFO MainThread Files in the images: 4
[2023-12-08 15:07:19,827] INFO MainThread Files in the video: 5
[2023-12-08 15:07:19,827] INFO MainThread Files in the documents: 14
[2023-12-08 15:07:19,827] INFO MainThread Files in the audio: 3
[2023-12-08 15:07:19,827] INFO MainThread Files in the archives: 10
[2023-12-08 15:07:19,827] INFO MainThread Files in the other: 3
[2023-12-08 15:07:19,827] INFO MainThread Total time: 0.6793093681335449
[2023-12-08 15:07:19,827] INFO MainThread Finished sorting folder C:\Work\test_for_sort
```
</details>

<details>
<summary>DEBUG level</summary>
 
```commandline
[2023-12-08 15:05:51,688] DEBUG MainThread Start time: 1702040751.6889925
[2023-12-08 15:05:51,688] INFO MainThread Started sorting folder C:\Work\test_for_sort
[2023-12-08 15:05:51,688] DEBUG Thread-1 (move_file) Created Folder C:\Work\test_for_sort\archives
[2023-12-08 15:05:51,694] DEBUG Thread-3 (move_file) Created Folder C:\Work\test_for_sort\documents
[2023-12-08 15:05:51,694] DEBUG Thread-4 (move_file) Normilized file-example_PDF_500_kB.pdf -> file_example_PDF_500_kB.pdf
[2023-12-08 15:05:51,694] DEBUG Thread-6 (move_file) Normilized file-sample_500kB.docx -> file_sample_500kB.docx
[2023-12-08 15:05:51,694] DEBUG Thread-7 (move_file) Normilized file-sample_500kB.odt -> file_sample_500kB.odt
[2023-12-08 15:05:51,694] DEBUG Thread-5 (move_file) Normilized file-sample_500kB.doc -> file_sample_500kB.doc
[2023-12-08 15:05:51,694] DEBUG Thread-3 (move_file) Normilized file-example_PDF_500_kB - Copy.pdf -> file_example_PDF_500_kB___Copy.pdf
[2023-12-08 15:05:51,694] DEBUG Thread-25 (move_file) Normilized file_таблиця.xls -> file_tablitsya.xls
[2023-12-08 15:05:51,704] DEBUG Thread-28 (move_file) Normilized resume-samples.pdf -> resume_samples.pdf
[2023-12-08 15:05:51,704] DEBUG Thread-29 (move_file) Normilized ПрезентацІЯ_500kB.ppt -> PrezentatsIYa_500kB.ppt
[2023-12-08 15:05:51,845] DEBUG Thread-19 (move_file) File moved C:\Work\test_for_sort\file_example_PPT_500kB.ppt -> C:\Work\test_for_sort\documents\file_example_PPT_500kB.ppt
[2023-12-08 15:05:51,845] DEBUG Thread-27 (move_file) Normilized old.pdf.zip -> old_pdf.zip
[2023-12-08 15:05:51,845] DEBUG Thread-7 (move_file) File moved C:\Work\test_for_sort\file-sample_500kB.odt -> C:\Work\test_for_sort\documents\file_sample_500kB.odt
[2023-12-08 15:05:51,845] DEBUG Thread-1 (move_file) File moved C:\Work\test_for_sort\1.zip -> C:\Work\test_for_sort\archives\1.zip
[2023-12-08 15:05:51,845] DEBUG Thread-5 (move_file) File moved C:\Work\test_for_sort\file-sample_500kB.doc -> C:\Work\test_for_sort\documents\file_sample_500kB.doc
[2023-12-08 15:05:51,845] DEBUG Thread-16 (move_file) File moved C:\Work\test_for_sort\file_example_ODS_1000.ods -> C:\Work\test_for_sort\documents\file_example_ODS_1000.ods
[2023-12-08 15:05:51,845] DEBUG Thread-3 (move_file) File moved C:\Work\test_for_sort\file-example_PDF_500_kB - Copy.pdf -> C:\Work\test_for_sort\documents\file_example_PDF_500_kB___Copy.pdf
[2023-12-08 15:05:51,845] DEBUG Thread-18 (move_file) Created Folder C:\Work\test_for_sort\images
[2023-12-08 15:05:51,845] DEBUG Thread-6 (move_file) File moved C:\Work\test_for_sort\file-sample_500kB.docx -> C:\Work\test_for_sort\documents\file_sample_500kB.docx
[2023-12-08 15:05:51,845] DEBUG Thread-28 (move_file) File moved C:\Work\test_for_sort\resume-samples.pdf -> C:\Work\test_for_sort\documents\resume_samples.pdf
[2023-12-08 15:05:51,845] DEBUG Thread-25 (move_file) File moved C:\Work\test_for_sort\file_таблиця.xls -> C:\Work\test_for_sort\documents\file_tablitsya.xls
[2023-12-08 15:05:51,845] DEBUG Thread-17 (move_file) Created Folder C:\Work\test_for_sort\audio
[2023-12-08 15:05:51,845] DEBUG Thread-30 (move_file) Created Folder C:\Work\test_for_sort\video
[2023-12-08 15:05:51,845] DEBUG Thread-23 (move_file) File moved C:\Work\test_for_sort\file_example_XLSX_1000.xlsx -> C:\Work\test_for_sort\documents\file_example_XLSX_1000.xlsx
[2023-12-08 15:05:51,845] DEBUG Thread-2 (move_file) File moved C:\Work\test_for_sort\2.zip -> C:\Work\test_for_sort\archives\2.zip
[2023-12-08 15:05:51,845] DEBUG Thread-9 (move_file) File moved C:\Work\test_for_sort\file_example_CSV_5000.csv -> C:\Work\test_for_sort\documents\file_example_CSV_5000.csv
[2023-12-08 15:05:51,845] DEBUG Thread-13 (move_file) Created Folder C:\Work\test_for_sort\audio
[2023-12-08 15:05:51,845] DEBUG Thread-12 (move_file) Created Folder C:\Work\test_for_sort\video
[2023-12-08 15:05:51,845] DEBUG Thread-14 (move_file) Created Folder C:\Work\test_for_sort\video
[2023-12-08 15:05:51,845] DEBUG Thread-29 (move_file) File moved C:\Work\test_for_sort\ПрезентацІЯ_500kB.ppt -> C:\Work\test_for_sort\documents\PrezentatsIYa_500kB.ppt
[2023-12-08 15:05:51,845] DEBUG Thread-24 (move_file) File moved C:\Work\test_for_sort\file_example_XLS_1000.xls -> C:\Work\test_for_sort\documents\file_example_XLS_1000.xls
[2023-12-08 15:05:51,845] DEBUG Thread-8 (move_file) Created Folder C:\Work\test_for_sort\video
[2023-12-08 15:05:51,845] DEBUG Thread-15 (move_file) Created Folder C:\Work\test_for_sort\other
[2023-12-08 15:05:51,845] DEBUG Thread-11 (move_file) Created Folder C:\Work\test_for_sort\images
[2023-12-08 15:05:51,845] DEBUG Thread-10 (move_file) Created Folder C:\Work\test_for_sort\images
[2023-12-08 15:05:51,845] DEBUG Thread-4 (move_file) File moved C:\Work\test_for_sort\file-example_PDF_500_kB.pdf -> C:\Work\test_for_sort\documents\file_example_PDF_500_kB.pdf
[2023-12-08 15:05:51,845] DEBUG Thread-31 (move_file) Created Folder C:\Work\test_for_sort\images
[2023-12-08 15:05:51,845] DEBUG Thread-20 (move_file) Created Folder C:\Work\test_for_sort\other
[2023-12-08 15:05:51,845] DEBUG Thread-22 (move_file) Created Folder C:\Work\test_for_sort\video
[2023-12-08 15:05:51,845] DEBUG Thread-21 (move_file) Created Folder C:\Work\test_for_sort\audio
[2023-12-08 15:05:51,845] DEBUG Thread-26 (move_file) Created Folder C:\Work\test_for_sort\other
[2023-12-08 15:05:51,845] DEBUG Thread-27 (move_file) File moved C:\Work\test_for_sort\old.pdf.zip -> C:\Work\test_for_sort\archives\old_pdf.zip
[2023-12-08 15:05:51,861] DEBUG Thread-18 (move_file) File moved C:\Work\test_for_sort\file_example_PNG_500kB.png -> C:\Work\test_for_sort\images\file_example_PNG_500kB.png
[2023-12-08 15:05:51,861] DEBUG Thread-30 (move_file) Normilized файл відео_700kB.mov -> fayl_video_700kB.mov
[2023-12-08 15:05:51,861] DEBUG Thread-17 (move_file) File moved C:\Work\test_for_sort\file_example_OOG_1MG.ogg -> C:\Work\test_for_sort\audio\file_example_OOG_1MG.ogg
[2023-12-08 15:05:51,861] DEBUG Thread-12 (move_file) File moved C:\Work\test_for_sort\file_example_MOV_480_700kB.mov -> C:\Work\test_for_sort\video\file_example_MOV_480_700kB.mov
[2023-12-08 15:05:51,861] DEBUG Thread-14 (move_file) File moved C:\Work\test_for_sort\file_example_MP4_480_1_5MG.mp4 -> C:\Work\test_for_sort\video\file_example_MP4_480_1_5MG.mp4
[2023-12-08 15:05:51,861] DEBUG Thread-13 (move_file) File moved C:\Work\test_for_sort\file_example_MP3_1MG.mp3 -> C:\Work\test_for_sort\audio\file_example_MP3_1MG.mp3
[2023-12-08 15:05:51,861] DEBUG Thread-8 (move_file) File moved C:\Work\test_for_sort\file_example_AVI_480_750kB.avi -> C:\Work\test_for_sort\video\file_example_AVI_480_750kB.avi
[2023-12-08 15:05:51,861] DEBUG Thread-15 (move_file) File moved C:\Work\test_for_sort\file_example_ODP_500kB.odp -> C:\Work\test_for_sort\other\file_example_ODP_500kB.odp
[2023-12-08 15:05:51,861] DEBUG Thread-11 (move_file) File moved C:\Work\test_for_sort\file_example_JPG_500kB.jpg -> C:\Work\test_for_sort\images\file_example_JPG_500kB.jpg
[2023-12-08 15:05:51,861] DEBUG Thread-31 (move_file) Normilized файл_зображення.jpg -> fayl_zobrazhennya.jpg
[2023-12-08 15:05:51,861] DEBUG Thread-10 (move_file) File moved C:\Work\test_for_sort\file_example_GIF_500kB.gif -> C:\Work\test_for_sort\images\file_example_GIF_500kB.gif
[2023-12-08 15:05:51,861] DEBUG Thread-20 (move_file) File moved C:\Work\test_for_sort\file_example_TIFF_1MB.tiff -> C:\Work\test_for_sort\other\file_example_TIFF_1MB.tiff
[2023-12-08 15:05:51,861] DEBUG Thread-26 (move_file) Normilized old.pdf.rar -> old_pdf.rar
[2023-12-08 15:05:51,861] DEBUG Thread-22 (move_file) File moved C:\Work\test_for_sort\file_example_WMV_480_1_2MB.wmv -> C:\Work\test_for_sort\video\file_example_WMV_480_1_2MB.wmv
[2023-12-08 15:05:51,861] DEBUG Thread-21 (move_file) File moved C:\Work\test_for_sort\file_example_WAV_1MG.wav -> C:\Work\test_for_sort\audio\file_example_WAV_1MG.wav
[2023-12-08 15:05:51,861] DEBUG Thread-30 (move_file) File moved C:\Work\test_for_sort\файл відео_700kB.mov -> C:\Work\test_for_sort\video\fayl_video_700kB.mov
[2023-12-08 15:05:51,876] DEBUG Thread-31 (move_file) File moved C:\Work\test_for_sort\файл_зображення.jpg -> C:\Work\test_for_sort\images\fayl_zobrazhennya.jpg
[2023-12-08 15:05:51,876] DEBUG Thread-26 (move_file) File moved C:\Work\test_for_sort\old.pdf.rar -> C:\Work\test_for_sort\other\old_pdf.rar
[2023-12-08 15:05:51,876] DEBUG Thread-52 (move_file) File moved C:\Work\test_for_sort\subf_level1\subfolder_level2\subfolder_level3\subfolder_level4\123.txt -> C:\Work\test_for_sort\documents\123.txt
[2023-12-08 15:05:51,876] DEBUG MainThread All threads finished
[2023-12-08 15:05:51,876] INFO MainThread Starting unpacking archives
[2023-12-08 15:05:51,907] DEBUG Thread-59 (unpack_archive) Archive unpacked C:\Work\test_for_sort\archives\2.zip -> C:\Work\test_for_sort\archives\2
[2023-12-08 15:05:51,907] DEBUG Thread-58 (unpack_archive) Archive unpacked C:\Work\test_for_sort\archives\1.zip -> C:\Work\test_for_sort\archives\1
[2023-12-08 15:05:51,907] DEBUG Thread-60 (unpack_archive) Archive unpacked C:\Work\test_for_sort\archives\old_pdf.zip -> C:\Work\test_for_sort\archives\old_pdf
[2023-12-08 15:05:51,907] DEBUG MainThread All threads finished
[2023-12-08 15:05:51,907] INFO MainThread Deleting empty folders
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subfolder_level1\subfolder_level2\subfolder_level3\subfolder_level4
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subfolder_level1\subfolder_level2\subfolder_level3
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subfolder_level1\subfolder_level2
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subf_level1\subfolder_level2\subfolder_level3\subfolder_level4
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subf_level1\subfolder_level2\subfolder_level3
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subf_level1\subfolder_level2
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subfolder_level1
[2023-12-08 15:05:51,907] DEBUG MainThread Empty Folder was removed C:\Work\test_for_sort\subf_level1
[2023-12-08 15:05:51,907] INFO MainThread Counting files in folders C:\Work\test_for_sort
[2023-12-08 15:05:51,907] INFO MainThread ------------------------- Sorting results -------------------------
[2023-12-08 15:05:51,907] INFO MainThread Known extensions: .xlsx, .gif, .zip, .mp4, .csv, .jpg, .docx, .ppt, .ogg, .png, .avi, .xls, .txt, .mp3, .odt, .doc, .wav, .wmv, .mov, .ods, .pdf
[2023-12-08 15:05:51,907] INFO MainThread Unknown extensions: .rar, .tiff, .odp
[2023-12-08 15:05:51,923] INFO MainThread Files in the images: 4
[2023-12-08 15:05:51,923] INFO MainThread Files in the video: 5
[2023-12-08 15:05:51,923] INFO MainThread Files in the documents: 14
[2023-12-08 15:05:51,923] INFO MainThread Files in the audio: 3
[2023-12-08 15:05:51,923] INFO MainThread Files in the archives: 10
[2023-12-08 15:05:51,923] INFO MainThread Files in the other: 3
[2023-12-08 15:05:51,923] DEBUG MainThread End time: 1702040751.9235134
[2023-12-08 15:05:51,923] INFO MainThread Total time: 0.23452091217041016
[2023-12-08 15:05:51,923] INFO MainThread Finished sorting folder C:\Work\test_for_sort
```
</details>

### Additional notes:

The script uses the transliteration dictionary to normalize filenames for non-English characters. This dictionary can be customized to your specific needs.
The script can be extended to support additional features, such as file size limits for each category.
