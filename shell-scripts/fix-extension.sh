for file in *.mov; do
    mv -- "$file" "${file%.mov}.mp4"
done