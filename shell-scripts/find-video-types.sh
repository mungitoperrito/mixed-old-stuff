# -x

SAVE_ROOT=/Users/davecuthbert/tmp/fotos

# Run this in the videos directory to sort the different video types

# for f in $(ls | head -5) # DEBUG
for f in $(ls)
do
   # echo ${f} # DEBUG
   file_type=$(file ${f} | cut -d ' ' -f 2-4)
   # echo "${file_type}   ${ft}" # DEBUG

   case ${file_type} in

      "ISO Media")
      cp ${f} ${SAVE_ROOT}/video/avi
      ;;

      "ISO Media, Apple")
      cp ${f} ${SAVE_ROOT}/video/mov
      ;;

      "ISO Media, HEIF")
      cp ${f} ${SAVE_ROOT}/video/avci
      ;;

      "ISO Media, MP4")
      cp ${f} ${SAVE_ROOT}/video/mp4
      ;;

      *)
      # echo "Ignore"  # DEBUG
      ;;
  esac
done
