"""仮想のブロックチェーンを作ってみる"""

class Blockchain(object()):
    
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
        
        def new_block(self):
            """新しいブロックを生成してチェーンに入る"""
            pass
    
    @staticmethod()
    def hash(block):
        """ブロックのハッシュ値を出力する"""
        pass
    
    @property()
    def last_block(self):
        """チェーンの最後ブロックを返却"""
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        リストに取引を追加し、追加されるブロックのインデックスを返却する
        
        sender : 送信者のアドレス
        recipient : 受信者のアドレス
        amount :
        
        return : 当取引のブロック数
        """
        self.current_transactions.append({
                'sender' : sender,
                'recipient' : recipient,
                'amount' : amount,
            })
        
        return self.last_block['index'] + 1
    
    def new_block(self, proof, previous_hash=None):
        #return block
        print()