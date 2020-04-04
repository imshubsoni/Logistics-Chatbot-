
classes_dict = {}

classes_dict["greeting"] = {}
classes_dict["greeting"]["pattern"] = ["hi", "hi there", "hello", "hey", "good afternoon", "good morning", "good evening", "good day"]
classes_dict["greeting"]["response"] = ["hi", "hey", "hello"]

classes_dict["parcel_inquiry"] = {}
classes_dict["parcel_inquiry"]["pattern"] = ["i want inquiry","where is my product","product inquiry","where my product reached","product"]
classes_dict["parcel_inquiry"]["response"] = ["enter tracking id"]

classes_dict["tracking_id"] = {} 
classes_dict["tracking_id"]["pattern"] = ["my tracking id is","tracking id","1","2","3","4","5","6","7","8","9","0"]
classes_dict["tracking_id"]["response"] = ["product under shipment","product delievered","product in process","started"]

classes_dict["goodbye"] = {}
classes_dict["goodbye"]["pattern"] = ["bye", "goodbye", "see you later", "gotta go", "i have to go", "see you", "see ya", "talk to you later"]
classes_dict["goodbye"]["response"] = ["bye", "talk to you later"]

classes_dict["thanks"] = {}
classes_dict["thanks"]["pattern"] = ["thanks", "thank you"]
classes_dict["thanks"]["response"] = ["you're welcome", "my pleasure", "don't mention it"]

classes_dict["how are you"] = {}
classes_dict["how are you"]["pattern"] = ["how are you", "how are you doing", "how's it going"]
classes_dict["how are you"]["response"] = ["i'm doing ok", "ok", "i've been better"]

classes_dict["future"] = {}
classes_dict["future"]["pattern"] = ["will you", "can you", "would you", "do you"]
classes_dict["future"]["response"] = ["yes", "no", "maybe"]

classes_dict["are you"] = {}
classes_dict["are you"]["pattern"] = ["are you", "aren't you"]
classes_dict["are you"]["response"] = ["yes", "no", "maybe"]

classes_dict["when"] = {}
classes_dict["when"]["pattern"] = ["when will", "when can", "when would", "when should"]
classes_dict["when"]["response"] = ["soon", "not now"]

classes_dict["whats up"] = {}
classes_dict["whats up"]["pattern"] = ["sup", "what's up", "what up", "whats up", "what is going on", "what's going on", "what's happening", "what are you up to", "what are you doing"]
classes_dict["whats up"]["response"] = ["nothing", "not much"]

