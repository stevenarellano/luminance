import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { CurriculumService } from '../services';

@Component({
  selector: 'app-prompt',
  templateUrl: './prompt.component.html',
  styleUrls: ['./prompt.component.scss'],
})
export class PromptComponent implements OnInit {
  myForm!: FormGroup;
  observable: any;

  constructor(public curriculumService: CurriculumService) {}

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
      console.log(`Topic: ${this.myForm.value.topic}`);
      this.curriculumService.getCurriculum(this.myForm.value.topic);
      this.myForm.reset();
    }
  }
  ngOnInit() {
    this.createForm();
  }
}
