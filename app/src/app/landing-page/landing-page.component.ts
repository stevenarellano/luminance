import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss'],
})
export class LandingPageComponent implements OnInit {
  myForm!: FormGroup;
  observable: any;

  constructor(private http: HttpClient) {}

  createForm() {
    this.myForm = new FormGroup({
      topic: new FormControl('', [Validators.required]),
    });
  }

  get topic(): FormControl {
    return this.myForm.get('topic') as FormControl;
  }

  onSubmit() {
    if (this.myForm.valid) {
      console.log(`Topic: ${this.topic.value}`);
      this.myForm.reset();
    }
    console.log(this.http.get('http://ip.jsontest.com/'));
    this.observable = this.http.get('http://ip.jsontest.com/');
  }

  ngOnInit() {
    this.createForm();
  }
}

export interface TopicPrompt {
  topic: string;
}
