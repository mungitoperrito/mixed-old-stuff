# Create directories

# Run this in the save directory

EXT=".jpg"

th=0
h=0
t=0
o=1
for file in $(ls)
do
  # echo "${th} ${h} ${t} ${o}" # DEBUG

  mv ${file} ${th}${h}${t}${o}${EXT}
  echo $((o++)) > /dev/null
  if [[ o -eq 10 ]]
  then
    o=0
    echo $((t++)) > /dev/null
  fi

  if [[ t -eq 10 ]]
  then
    t=0
    echo $((h++)) > /dev/null
  fi

  if [[ h -eq 10 ]]
  then
    h=0
    echo $((th++)) > /dev/null
  fi

    if [[ th -eq 10 ]]
  then
    echo "PANIC NEED TEN THOUSANDS"
  fi
done