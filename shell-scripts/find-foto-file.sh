# -x

# Start at the top level directory
SAVE_ROOT=/Users/davecuthbert/tmp/fotos

DIR_LIST=$(ls -d */)
# echo ${DIR_LIST} # DEBUG

# DEBUG
# count=0  # DEBUG
for d in ${DIR_LIST}
do
   cd ${d}
   echo -n "${d} "
   # for f in $(ls | head -5) # DEBUG
   for f in $(ls)
   do
      echo ${f} # DEBUG
      file_type=$(file ${f} | cut -d ' ' -f 2-3)
      ft=${file_type//,}
      # echo "${file_type}   ${ft}" # DEBUG

      case ${ft} in

         "JPEG image")
         # echo "${f} is a jpg" # DEBUG
         cp ${f} ${SAVE_ROOT}/jpg/
         ;;

         "PNG image")
         # echo "${f} is a png" # DEBUG
         cp ${f} ${SAVE_ROOT}/png/
         ;;

         "ISO Media")
         # echo "${f} is a video" # DEBUG
         cp ${f} ${SAVE_ROOT}/video/
         ;;

         *)
         # echo "Ignore"  # DEBUG
         ;;
     esac
   done
   cd ${TOP_LEVEL}

   # if [[ $((count++)) -eq 3 ]] ; then break ; fi # DEBUG
done