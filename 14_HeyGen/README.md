# TLDR

HeyGen baby!

## Links

- https://app.heygen.com/ (HeyGen portal)
- https://docs.heygen.com/ (HeyGen API)
- https://docs.heygen.com/docs/create-video#2-generate-video (Great documentation from HeyGen)

## How to use this project

1st sign up for HeyGen on the https://app.heygen.com/ site and create your personalized A.I. avatar in minutes.

2nd get a HeyGen API key from the https://docs.heygen.com/ site

```sh
export HEYGEN_API_KEY="<YOUR_HEYGEN_API_KEY_HERE>"
```

3nd run any one of the included scripts (hopefully the names are intuitive)

```sh
./14_HeyGen/scripts/list_avatars.sh # for finding the avatar id you'd like to use
./14_HeyGen/scripts/list_voices.sh # for finding the voice you'd like to pair with your avatar
./14_HeyGen/scripts/generate_video.sh # plug your desired avatar_id & voice_id here to generate custom Avatar videos
./14_HeyGen/scripts/check_video_generation_status.sh # for checking on the status of your video while it is being generated
```

## TIP

In the `./14_HeyGen/scripts/generate_video.sh` script replace `avatar_id` and `voice_id` with your preferred ids

- Example Avatar id: 148aa78267f84bdb8c88035378334c6d (ie: "Tad Duval's" v1 avatar)
- Example Voice id: e7e6ad7c235748fe9147884f26c3af94 (ie: "Tad Duval's" v1 voice)
