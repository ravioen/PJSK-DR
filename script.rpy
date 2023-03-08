# defines characters
# characters use their stage outfits


# deleted later
# in order to create menus (example)
# menu:
#   "AAAAAAAA": 
#       jump variable
#   "ew":
#       jump var2
# label variable
#   blah blah blah
#   jump var3*
# label var2
#   blah blah blah
#   jump var3

#Intalics:  "{i}---{/i}"
# *this is so you can return back to normal story


define ic = Character("Ichika")
define sa = Character("Saki")
define ho = Character("Honami")
define shh = Character("Shiho")
define minn = Character("Minori")
define ha = Character("Haruka")
define ai = Character("Airi")
define shz = Character("Shizuki")
define ko = Character("Kohane")
define an = Character("An")
define toy = Character("Toya")
define ginger = Character("Akito")
define star = Character("Tsukasa")
define ru = Character("Rui")
define ne = Character("Nene")
define em = Character("Emu")
define ka = Character("Kanade")
define ma = Character("Mafuyu")
define yu = Character("Yuki")
define miz = Character("Mizuki")
define en = Character("Ena")
define mik = Character("Miku")
define rin = Character("Rin")
define len = Character("Len")
define lu = Character("Luka")
define mei = Character("MEIKO")
define kai = Character("KAITO")

# general "unknown" character
define uk = Character("???")


# The game starts here.
label start:

    # bg
    scene bg classroom
    with dissolve


    # nene wakes up from her sleep
    show nene sleep
    ne ""
    show nene confuse
    ne "..huh?"
    "(I raised my head from a desk I don’t remember sleeping on. My body still felt heavy from sleep.)"
    "(Why was I here? I thought I was just in my room, playing a few games.)"
    show nene think
    "(No, wait. My troupe had agreed to meet in our SEKAI for practice so we didn’t have to do it in the snow, and I tapped on The World Hasn’t Even Started Yet. I pressed play and it faded to white as normal, but then my memory cuts out.)"
    "(Looking around, a note caught my eye. It’s right next to my arms, and it was placed, seemingly deliberately, on the desk. It was very obviously addressed to me on the outside.)"
    hide nene think
    
    # note
    uk "Good morning, Nene!"
    uk "Welcome to the first day of the rest of our lives, and don’t forget that we have an assembly later! I’m sure you can find the gym easily enough."
    uk "Before I forget, you will need to know one piece of information. For the sake of authenticity, you’re now the Ultimate Diva! Don’t forget to include this when you introduce yourself. It’s not like there will be any consequences, but we prefer it this way."
    uk "We’ll see you soon :)"
    show nene surprise
    ne "Rest of our lives?? What the hell???"
    hide nene surprise
    
    # emu wakens
    uk "Yawn... Nene-chan? Where are we?"
    "(I look over to my left to see a familiar friend: Emu Otori. Immediately, I hopped up to head to her. As I did, I noticed that I was in my PXL uniform, and so was Emu.)"
    show nene surprise
    ne "Emu! Are you okay?"
    hide nene surprise
    
    # emu note
    show emu smile
    em "Yupyup! Oo, I have a letter!!"
    hide emu smile
    "(Ah, seems like she noticed it.. I wonder if her’s is any different from mine.)"
    show emu negspiral
    em "WAAH!! WE CAN’T LEAVE???"
    hide emu negspiral
    "(..Apparently not. I’m not sure how to calm her down though—)"
    show emu smile
    em "Oo!! I’m the Ultimate Clown!!!!"
    hide emu smile
    "(That was quick. I don’t know what I expected. Clown, though?)"
    show nene think
    ne "That feels backhanded."
    hide nene think
    show emu smug
    em "Huh?? No!! Clowns make people smile!! And I’m one too!!!"
    hide emu smug
    show nene think
    ne "Heh, that’s fair… I think we should find the gym though. I… don’t want to anger whoever did this."
    hide nene think
    show emu smile
    em "Mhm mhm!! Operation “find-the-gym” is a go!!!"

    # hallway
    scene bg black
    with dissolve
    "(Emu and I went into the hall, and one thing was pretty comforting. Though, this is one example of the cons outweighing the pros. We were in Kamikou, but everything was…off.)"

    scene bg hallway
    with dissolve
    "(Some classrooms were changed from their original purpose, but I’m not sure to what. The windows were all blocked with metal. It felt like a prison.)"
    show nene think
    ne "We’re in Kamiyama. Follow me."
    hide nene think
    show emu smile
    em "Oo!! Hehe, maybe I can find a new way to sneak in~!"
    hide emu smile
    "(I couldn’t help the fact that her scheming made me smile a bit; her joy’s always so contagious.)"

    # gym
    show bg black
    with dissolve
    "(Eventually, we got to the gym. It seems like Emu and I were the last ones to arrive. I think there are 18 others; some that I recognize, and others I don’t. Speaking of which…)"
    show bg gym
    with dissolve
    uk "20. Considering we all are apart of some sort of group, I think that’s the last of new arrivals."
    "(Rui. Not even surpised that he was the one to assume that all of us were here. It looks like both him and Tsukasa are also in their PXL uniforms.)"
    uk "Alright then, how about some introductions? Let’s all get into a circle by group~!"
    "(Ah, Mizuki. I’m glad to see that they’re much more confident now, and much happier too.)"
    "(Everyone moved to sit in a circle on the gym floor, seemingly by group. Just as Mizuki requested.)"
    mi "Black hair, you should start!"
    
    # leo/need
    uk "Ah, alright.. I’m Ichika Hoshino, the Ultimate Guitarist! I’m apart of Leo/Need."
    uk "Saki Tenma! I’m the Ultimate Pianist, and the keyboardist in Leo/Need!!"
    uk "Honami Mochizuki, Ultimate Drummer for Leo/Need!"
    uk "Shiho Hinomori, Ultimate Bass Guitarist."
    
    # mmj
    uk "Minori Hanasoto! Uhm, I was assigned the Ultimate Unlucky Student… But, I’m apart of More More Jump! and trying to work past it!"
    "(That’s gotta hurt…)"
    uk "Ah, sorry again, Minori…"
    minn "Don’t worry, Haruka, you weren’t in control of it!"
    ha "Of course, but I still feel bad. Oh, and I’m Haruka Kiritani, the Ultimate Idol and a member of More More Jump!!"
    uk "Airi Momoi! Ultimate Dancer!"
    uk "Shizuku Hinomori! I’m the Ultimate Model, and the older sister of Shiho!"
    "(I looked over and saw Shiho bashfully pouting.)"
    
    # vbs
    uk "Uhm… K-Kohane Azusawa, the Ultimate Photographer..! I’m apart of Vivid Bad Squad, too."
    uk "An Shiraishi, the Ultimate Singer and also apart of Vivid Bad Squad!"
    uk "Toya Aoyagi, the Ultimate Street Artist. It’s a pleasure to meet all of you."
    uk "Akito Shinonome, Ultimate Beatboxer."
    
    # wxs
    "(Well, now it’s Tsukasa’s turn. My turn’s coming up soon… Wait, I didn’t realize that Rui and Tsukasa were sitting next to each other until now. Huh, weird. I’m just glad that they’re getting close. Don’t want a repeat of middle school…)"
    star "Tsukasa Tenma, the Ultimate Actor and a world future star!! I’m also the lead actor for Wonderlands x Showtime and the greatest brother in the world!"
    "(I still wonder how him and Emu actually make those sparkles and such. I asked Emu, but she only told me that you “have to be wonderhoy enough!”. That was a bit vague for me…)"
    "(It seems that Saki, Toya, and a girl with long, white hair all fondly smiled at his last comment. When did the Tenma family grow again? I don’t remember that girl.)"
    ru "Rui Kamishiro, the Ultimate Inventor! I’m also the director at Wonderlands x Showtime."
    show emu smile
    em "Emu Otori, the Ultimate Clown and a proud member of Wonderlands x Showtime! Wan-wan… WONDAHOI!!!"
    hide emu smile
    show nene think
    ne "N-Nene Kusanagi… Ultimate Diva and apart of Wonderlands x Showtime…. Ah, she/they, please."
    hide nene think
    "(It… wasn’t that bad to introduce myself to these 16-ish new people. Everyone showed interest in what I said. Maybe this group wont be too bad to be here with.)"
    
    # ji
    uk "U-uhm… Kanade Yoisaki… Ultimate Composer…"
    "(Ah, so the newest Tenma is Kanade.)"
    mi "K~… Don’t forget that you’re apart of N25!"
    ka "Ah.. yeah, I’m the composer for N25…"
    uk "I’m Mafuyu Asahina! My Ultimate was just left as 3 question marks, but I’m also apart of N25."
    "(I vaguely saw Mizuki lightly jab Mafuyu, before some sort of realization hit her.)"
    ma "Ah! I also use he/they pronouns and do identify more closely as a male. I hope you all will make to remember this!"
    "(…Now I feel shitty. Sorry Mafuyu. I guess I’m not used to meeting other trans people…)"
    "(I saw Mizuki smile again, and we moved on…again. I guess they’re the one to make sure people don’t forget anything in their group.)"
    miz "Mizuki Akiyama, they/them! I’m also the Ultimate Animator, and the music video artist for N25! Oh, and Yuki right here is my adorable boyfriend, so don’t try and take him~!"
    "(I saw Mizuki clinging to Mafuyu — is Yuki a preferred name? — and them very lightly blushing in return. They were obviously messing around, but I’m not sure if everyone got the memo...)"
    uk "Ahem. Ignoring those two, I’m Ena Shinonome, the Ultimate Artist! I’m also apart of N25, and regrettably the older sister of Akito over there."
    "(I looked over and saw Akito rolling his eyes.)"
    
    # miku shows ooOEoO
    uk "Fufufu~ Looks like everyone’s acquainted!"
    "(Everyone turned towards the stage, but no one was there.)"
    ko "…huh?"
    # miku shows up here
    mik "Welcome, everyone, to the rest of your lives! I’m Hatsune Miku, as you of course know, and I’ll be your headmaster! I hope you’re ready to spend each day until your inevitable death here~."
    mik "I s’pose I better explain the predicament you all find yourselves in now! Don’t want anyone to get frustrated at me for not explaining."
    "(She quickly glared off to the side, before returning back to her cheery disposition. I couldn’t even feel the joy, everything about it felt fake…)"
    "You’re all trapped here for the rest of your lives, here in this SEKAI based around Kamiyama High! Or, well~♪…"
    en "Well? Get on with it!"
    mik "Fine, fine! Bratty, much? Well then, you’re all here forever and ever and ever… {i}unless{/i} you kill someone!"
    "(You could hear a pin drop. I just barely realized that I had begun to hold my breath.)"
    "({i}Kil{/i} someone? Who would be so desperate to get out that they’d murder another person? Especially in a group where everyone you know at least knows someone who knows who you killed…)"
    mik "If you end up killing someone, you and your group can go back to regular life! A comforting thought, isn’t it?"
    mik "Oh, and before you decide to reach for your phones and stop whatever song born of your feelings, don’t! We have your phones hidden ni~ce and well~♪!"
    ginger "What the hell are you talking about?! You can’t just trap us here, that’s illegal!"
    toy "Akito, I don’t think she cares. This isn’t our Miku…"
    "(Akito scowled at that, obviously holding himself back from saying more. I think kind Akito is still scarier, though.)"
    ma "…Who’s "we"?"
    mik "Ah, of course! Ev~eryone~♪! It’s time for introductions~♪!"
    mik "These are the teachers during your stay here! Do any of you {i}not{/i} know who these people are? No? Good! I’m not trying to be here longer than I have to."
    kai "Miku."
    mik "Oh, shut it, KAITO. Hows about you 5 hand out the handbooks {i}they{/i} took so long to make?"
    kai "… Fine. Does everyone remember their group assignments?"
    "(The rest of the group nodded, and they went off stage to hand out our “handbooks”. Was the school theme {i}really{/i} necessary?)"
    "((Luka went towards Leo/Need, and she seemed half asleep as she gave the 4 their handbooks. I think I even spotted them trading theirs as soon as they turned the strange devices on. Rin and Len, in a weird sync, passed out theirs to More More Jump! and Vivid Bad Squad respectively. Regrettably, KAITO passed out ours. MEIKO passed out N25’s with a smile that will haunt my dreams later.)"
    mik "I implore you to read the rules, as all of them have the same punishment for breaking them. Well, except for rules 1 and 2; those are just guidelines, to be honest. {i}Unless{/i} you make your way into one of the off limit areas. Then the punishment is the same as all the other rules!"
    "(I open up the weird contraption they’re calling our handbooks. It’s strangely advanced. I flipped to the rules section and was about to read it, when suddenly…)"
    star "Rui, no!! We need these!!"
    "(I looked up to see Tsukasa struggling to hold Rui’s wrists away from the handbook that dropped on the floor, constantly having to grab one or the other again and again. I think he was trying to pull him away, but that’s…pretty hard. I still remember Rui carrying Nenerobo to me when she was finished…)"
    ru "{i}Tsukasa-kunnn!{/i} I have to see how this works! If we get out of here then—"
    star "{i}Theen,{/i} you’ll have the handbook and everything you need to dissect it! Not while we’re still here!!"
    "(Instead of focusing on… {i}that{/i}, I turned back to my handbook that had turned on. I could still see them out of the corner of my eye, but I just tuned them out. Actually, ignore everything I just said. KAITO just picked them up with the collar of their respective uniforms. Rui looked like a cat who was just picked up by the scruff of his neck, his limbs dangling with a stunned face and letting KAITO hold him, despite being obviously able to touch the ground if he tried. Tsukasa just stood up, followed by no objections from KAITO.)"
    nen "Hey, Emu, Rui looks like a cat."
    em "{i}gasp{/i}, he does!! Hehe, he looks so funny like that."
    "(After a chuckle, I turned back to my handbook. I vaguely saw Rui be dropped and fall into a proper sitting position. Dear god, he’s just like a cat…)"
    "(The rules were fairly standard; hardly as threatening as the apathetic Miku on the stage. The rules were as followed:"
    # possibly make this a reading thing? idk
    ({i}{b}Rule #1:{/b}"Nighttime" is from 10 pm to 7 am. Some areas are off-limits at night, so please exercise caution.{/i})
    ({i}{b}Rule #2:{/bWith minimal restrictions, you are free to explore this Kamiyama SEKAI at your discretion.{/i})
    ({i}{b}Rule #3:{/b}Violence against headmaster Miku or the teachers is strictly prohibited, as is destruction of surveillance cameras.{/i})
    # ... etc
    
    mik "In your handbook, you’ll find your dorm assignments. Your handbook acts as keys to your rooms, but we have backup keys if you get locked out. Or have a target in mind, fufufu~. We wont tell, of course!"
    ko "…N-no! I- I refuse to participate!!"
    mik "…Ms. Asuzawa, you absolutely {i}must{/i} participate in this. If you refuse, we’ll have you forcibly removed from the game."
    ko "T-then remove me…! This is inhumane!!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.
    return
