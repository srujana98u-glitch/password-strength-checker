{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d27e8cc7-ada0-4e1e-bcc4-7cd6b581243d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password:  Atas@123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Strong Password\n"
     ]
    }
   ],
   "source": [
    "password = input(\"Enter password: \")\n",
    "\n",
    "score = 0\n",
    "\n",
    "if len(password) >= 8:\n",
    "    score += 1\n",
    "else:\n",
    "    print(\"Password should be at least 8 characters\")\n",
    "\n",
    "if any(c.isupper() for c in password):\n",
    "    score += 1\n",
    "else:\n",
    "    print(\"Add at least one uppercase letter\")\n",
    "\n",
    "if any(c.islower() for c in password):\n",
    "    score += 1\n",
    "else:\n",
    "    print(\"Add at least one lowercase letter\")\n",
    "\n",
    "if any(c.isdigit() for c in password):\n",
    "    score += 1\n",
    "else:\n",
    "    print(\"Add at least one digit\")\n",
    "\n",
    "if score <= 2:\n",
    "    print(\"Weak Password\")\n",
    "elif score == 3:\n",
    "    print(\"Medium Password\")\n",
    "else:\n",
    "    print(\"Strong Password\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb96d93-93b8-4576-832e-246cb4fe4d5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
