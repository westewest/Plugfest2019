./interactive_face_detection_demo -i cam -d CPU -m intel_models/face-detection-retail-0004/FP32/face-detection-retail-0004.xml -m_ag intel_models/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.xml -m_em intel_models/emotions-recognition-retail-0003/FP32/emotions-recognition-retail-0003.xml -m_hp intel_models/head-pose-estimation-adas-0001/FP32/head-pose-estimation-adas-0001.xml -r | python3 /export/install/PRISM/DEMO/face_detection/face-mqtt.py -c /export/install/PRISM/DEMO/config.yml
