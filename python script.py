{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "820b079a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "078f4d59",
   "metadata": {},
   "outputs": [],
   "source": [
    "objects = []\n",
    "with (open(\"/home/sachin269/Downloads/set_0.pkl\", \"rb\")) as openfile:\n",
    "    while True:\n",
    "        try:\n",
    "            objects.append(pickle.load(openfile))\n",
    "        except EOFError:\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "18fdb93a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-6-ded4f4c851c5>:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working\n",
      "  from collections import Iterable\n"
     ]
    }
   ],
   "source": [
    "from collections import Iterable\n",
    "def flatten(lis):\n",
    "     for item in lis:\n",
    "         if isinstance(item, Iterable) and not isinstance(item, str):\n",
    "             for x in flatten(item):\n",
    "                 yield x\n",
    "         else:        \n",
    "             yield item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "58dbd1a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_object = list(flatten(objects))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9bf7b7ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_object.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b4f36ee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# textfile = open(\"/home/sachin269/Desktop/caption_new.txt\", \"w\")\n",
    "# for element in new_object:\n",
    "#     textfile.write(element + \"\\n\")\n",
    "# textfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c3fbe548",
   "metadata": {},
   "outputs": [],
   "source": [
    "image_captions = open(\"/home/sachin269/Desktop/caption_new.txt\").read().split('\\n')\n",
    "caption = {}\n",
    "for i in range(len(image_captions)-1):\n",
    "    id_capt = image_captions[i].split(\"\\t\")\n",
    "    id_capt[0] = id_capt[0][:len(id_capt[0])-2] \n",
    "    try:\n",
    "        caption[id_capt[0]].append(id_capt[1])\n",
    "    except:\n",
    "        caption[id_capt[0]] = [id_capt[1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "aa96aed0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25001"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(image_captions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d2512f6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pairs = [(key, value) \n",
    "#             for key, values in caption.items() \n",
    "#             for value in values ]\n",
    "# for pair in pairs:\n",
    "#     print(pair)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "300afa30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('1000268201_693b08cb0e.jpg',\n",
       " 'A child in a pink dress be climb up a set of stair in an entry way .')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pairs[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "a4c246f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "lis = []\n",
    "for i in range(len(pairs)):\n",
    "    str = ','.join(pairs[i])\n",
    "    lis.append(str)\n",
    "textfile = open(\"/home/sachin269/Desktop/caption_new.txt\", \"w\")\n",
    "for element in lis:\n",
    "    textfile.write(element + \"\\n\")\n",
    "textfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "171b2ac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number of jpg flies in Flicker8k: 8091\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "dir_Flickr_jpg = \"/home/sachin269/Desktop/Flicker8k_Dataset/\"\n",
    "jpgs = os.listdir(dir_Flickr_jpg)\n",
    "print(\"The number of jpg flies in Flicker8k: {}\".format(len(jpgs)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e45448f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(jpgs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e5d9924",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
