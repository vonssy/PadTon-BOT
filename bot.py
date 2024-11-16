import requests
import json
import os
from colorama import *
from datetime import datetime
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class PadTON:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'api-community-miniapp.padton.com',
            'Origin': 'https://miniapp.padton.com',
            'Pragma': 'no-cache',
            'Referer': 'https://miniapp.padton.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}PadTON - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def auth_signin(self, query: str):
        url = 'https://api-community-miniapp.padton.com/api/auth/signin-with-telegram-miniapp'
        data = json.dumps({"initData":query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']['accessToken']
            else:
                return None
        else:
            return None

    def users_me(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/users/me'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def loyality_wallet(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/loyalty-wallet'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def entry_requirements(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/entry-requirements/my-list'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def verify_requirements(self, token: str, require_id: str):
        url = f'https://api-community-miniapp.padton.com/api/entry-requirements/{require_id}/verify'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def notifications(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/notifications?isRead=false'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def read_notifications(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/notifications/read'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def farm_pool(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/farm-pool/current'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def start_farm(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/farm-pool'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def claim_farm(self, token: str, farm_id: str):
        url = f'https://api-community-miniapp.padton.com/api/farm-pool/{farm_id}/claim'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def lucky_spin(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/lucky-spin/profile'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def spin_wheel(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/lucky-spin/spin'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def missions(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/missions'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def start_missions(self, token: str, mission_id: str):
        url = f'https://api-community-miniapp.padton.com/api/missions/{mission_id}/start'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def claim_missions(self, token: str, mission_id: str):
        url = f'https://api-community-miniapp.padton.com/api/missions/{mission_id}/claim'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        if response.status_code in [200, 201]:
            result = response.json()
            if result and result['status']:
                return result['data']
            else:
                return None
        else:
            return None

    def process_query(self, query: str):

        token = self.auth_signin(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if token:
            wallet = self.loyality_wallet(token)
            if wallet:
                user = self.users_me(token)
                if user:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {wallet['totalBalance']} PATC {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            requirements = self.entry_requirements(token)
            if requirements is not None:
                for require in requirements:
                    require_id = require['id']
                    status = require['status']

                    if require is not None and status == 'PENDING':
                        verify = self.verify_requirements(token, require_id)
                        if verify and verify['status'] == 'SUCCESS':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Verify{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['code']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['info']['reward']} PATC {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Verify{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['code']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Already Required {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)


            notifications = self.notifications(token)
            if notifications is not None:
                self.read_notifications(token)


            farm = self.farm_pool(token)
            if farm is None:
                start = self.start_farm(token)
                if start is not None:
                    end_at = datetime.strptime(start['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                    end_at_wib = end_at.astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                farm = self.farm_pool(token)

            if farm is not None:
                farm_id = farm['id']

                end_at = datetime.strptime(farm['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                end_at_wib = end_at.astimezone(wib).strftime('%x %X %Z')

                now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)

                if now_utc >= end_at:
                    claim = self.claim_farm(token, farm_id)
                    if claim is not None:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim['loyaltyAmount']} PATC {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    time.sleep(1)

                    start = self.start_farm(token)
                    if start is not None:
                        end_at = datetime.strptime(start['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                        end_at_wib = end_at.astimezone(wib).strftime('%x %X %Z')
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

            lucky_spin = self.lucky_spin(token)
            if lucky_spin is not None:
                count = lucky_spin['totalSpin']
                while count > 0:
                    spin = self.spin_wheel(token)
                    if spin is not None:
                        reward = spin['amount']
                        symbol = spin['currencySymbol']
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {reward} {symbol} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Chances{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {count-1} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        count -= 1
                        time.sleep(1)
                    else:
                        break

                if count == 0:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Chance {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            missions = self.missions(token)
            if missions is not None:
                for mission in missions:
                    mission_id = mission['id']
                    status = mission['status']

                    if mission is not None and status == 'INIT':
                        start = self.start_missions(token, mission_id)
                        if start is not None and start['status'] == 'PENDING':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            time.sleep(3)

                            claim = self.claim_missions(token, mission_id)
                            if claim is not None and claim['status'] == 'SUCCESS':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['loyaltyReward']} PATC {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(2)

                    elif mission is not None and status == 'PENDING':
                        claim = self.claim_missions(token, mission_id)
                        if claim is not None:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['loyaltyReward']} PATC {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(2)

            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        time.sleep(3)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] PadTON - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = PadTON()
    bot.main()