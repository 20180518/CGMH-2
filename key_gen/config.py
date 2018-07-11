class config(object):
    def __init__(self):
        self.data_path='../data/1-billion/1-billion-train.mini.tok.pkl'               
        self.use_data_path='../data/1-billion/seed.txt'
        self.dict_path='../data/1-billion'
        self.emb_path='../data/1-billion/emb.pkl'
        self.pos_path='../POS/english-models'
        self.dict_size=50000
        self.vocab_size=50003
        self.forward_save_path='./model/forward.ckpt'
        self.backward_save_path='./model/backward.ckpt'
        self.forward_log_path='./log/forward_log.txt'
        self.backward_log_path='./log/backward_log.txt'
        self.use_fp16=False
        self.shuffle=False
        self.use_log_path='./log/use_log.txt'
        
        self.skipthoughts_path='../skip_thoughts'       #path of skipthoughts
        
        self.batch_size=32
        self.num_steps=50
        self.hidden_size=300
        
        self.keep_prob=1
        self.num_layers=2
        
        self.max_epoch=100
        self.max_grad_norm=5
        
        self.GPU='0'
        self.mode='use'
        self.sample_time=500
        self.record_time=[100,200,300]
        self.sample_sentence_number=119
        
        self.search_size=100
        self.use_output_path='./output/output_MH'
      
        #self.sample_prior=[1,1,1,1]
        self.action_prob=[0.3,0.3,0.3,0.1]
        #self.threshold=0.1
        self.sim=None
        #self.sim_word=True
        self.double_LM=False
        self.keyword_pos=False
        self.keyboard_input=False
        self.sim_hardness=5
        self.rare_since=30000
        self.just_acc_rate=0.0
        self.key_num=4
        self.min_length=7
        #self.max_suggest_word=20
