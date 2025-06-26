class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()  # 実際にメールが届くアドレスを格納する集合

        for email in emails:
            local, domain = email.split('@')  # ローカル名とドメイン名に分割

            # '+'以降を除去
            if '+' in local:
                local = local[:local.index('+')]

            # '.'を除去
            local = local.replace('.', '')

            # 最終的なアドレスを構築
            normalized_email = local + '@' + domain

            # セットに追加
            seen.add(normalized_email)

        return len(seen)  # ユニークなアドレス数を返す