//
//  ViewController.swift
//  FirstDefense
//
//  Created by Elena Sadler on 11/1/20.
//

import UIKit
import Alamofire

let siteCheckURL = "http://34.121.13.109:5000/?url="
var recordedResponse = "00000"

class ViewController: UIViewController {
    
    @IBOutlet weak var urlField: UITextField!
    
    @IBOutlet weak var assesmentViewOutlet: UIView!

    @IBOutlet weak var siteUsesHTTPS: UILabel!
    
    @IBOutlet weak var siteHasTooManyRedirects: UILabel!
    
    @IBOutlet weak var timeOutError: UILabel!
    
    @IBOutlet weak var possiblyPhishing: UILabel!
    
    @IBOutlet weak var targetDomainSameasDisplayed: UILabel!
    
    func handleResult(response: String){
        let usesHTTPS = response[0]
        let
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.

        
    }

    @IBAction func buttonPressed(_ sender: UIButton) {
        let inputURL = urlField.text
        AF.request(siteCheckURL + inputURL!).responseString { response in
            debugPrint("Response: \(response)")
            print("response: \(response)")
                   switch response.result {
                   case .success(let value):
                    self.handleResult(response: value)
                       
                   case .failure(let error):
                       print(error)
                   }
                }
        
        assesmentViewOutlet.isHidden = false
        print(recordedResponse + "this")
        
    }
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        urlField.endEditing(true)
        print(urlField.text!)
        return true
    }
    
}

