# onion-link-encryption
a lightweight encryptor used for hiding onion links

# instructions 
![image](https://github.com/sam40072/onion-link-encryption/assets/13662773/b1145d68-46b7-457e-811c-b6a812270c6a)

First you'll need to select the setup option, which will create a folder along with 3 text files.
You will need to select the amount of fake links and hashes to create, 1000 is a good number because its not too slow, but also not small enough to check by hand.

After the files were created, you can select the option for adding links, it will ask you to put in a link, which will then be stored with all the fake links and a hashed version of the link will be stored with the fake hashes

When you want to retrieve the links, you'll need to select the unhash option, which will list the original links

If you want to delete the files, just delete 4, and everything but the python file will be gone

# How it works
![image](https://github.com/sam40072/onion-link-encryption/assets/13662773/0c2bccbb-1e81-4355-9320-0018eb2508e4)

during setup, onionLinks.txt and fluff.txt get filled with fake information, after that is done, fluff.txt gets dumped into mainFile.txt. 

When a link is added, it gets appended to onionLink.txt and the hash of it gets appended to mainFile.txt.

When unhashing, fluff.txt gets compared to mainFile.txt and the links that are found in fluff.txt are eliminated leaving only the real hashes. Next onionLinks.txt gets hashed one by one, comparing it to the original hashes and when there is a match, it is printed to console. 

# disclaimer
This was a little project I made becacuse I wanted to try out the argon2 hashing
this is NOT the safest way to store onion links BY FAR so keep that in mind when using this
